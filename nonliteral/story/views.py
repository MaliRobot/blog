from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from functools import wraps
import json

from .models import Chapter, Choice, ReaderUser, UserProgress
from .forms import ReaderUserCreationForm, ReaderLoginForm


def reader_login_required(view_func):
    """Custom decorator to require reader login"""
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        if not hasattr(request, 'reader') or request.reader is None:
            messages.warning(request, "Please login to continue.")
            return redirect('story:reader_login')
        return view_func(request, *args, **kwargs)
    return wrapped_view


class ReaderLoginView(View):
    """Custom login view for ReaderUser"""
    template_name = 'story/reader_login.html'

    def get(self, request):
        if hasattr(request, 'reader') and request.reader:
            return redirect('story:dashboard')
        form = ReaderLoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ReaderLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                reader = ReaderUser.objects.get(username=username)
                if reader.check_password(password) and reader.is_active:
                    # Login successful
                    request.session['reader_user_id'] = reader.id
                    reader.last_login = timezone.now()
                    reader.save()

                    messages.success(request, f"Welcome back, {reader.get_full_name()}!")

                    # Redirect to next page or dashboard
                    next_page = request.GET.get('next', 'story:dashboard')
                    return redirect(next_page)
                else:
                    messages.error(request, "Invalid username or password.")
            except ReaderUser.DoesNotExist:
                messages.error(request, "Invalid username or password.")

        return render(request, self.template_name, {'form': form})


class ReaderLogoutView(View):
    """Custom logout view for ReaderUser"""

    def get(self, request):
        if 'reader_user_id' in request.session:
            del request.session['reader_user_id']
        messages.success(request, "You have been logged out.")
        return redirect('story:home')


class ReaderSignUpView(View):
    """Custom signup view for ReaderUser"""
    template_name = 'story/reader_signup.html'

    def get(self, request):
        if hasattr(request, 'reader') and request.reader:
            return redirect('story:dashboard')
        form = ReaderUserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ReaderUserCreationForm(request.POST)
        if form.is_valid():
            # Create new reader user
            reader = form.save(commit=False)
            reader.set_password(form.cleaned_data['password1'])

            # Set initial chapter
            first_chapter = Chapter.objects.first()
            if first_chapter:
                reader.current_chapter = first_chapter

            reader.save()

            # Log them in
            request.session['reader_user_id'] = reader.id
            reader.last_login = timezone.now()
            reader.save()

            messages.success(request, f"Welcome, {reader.get_full_name()}! Your adventure begins...")
            return redirect('story:dashboard')

        return render(request, self.template_name, {'form': form})


def home(request):
    """Landing page for the story application"""
    context = {
        'is_reader_logged_in': hasattr(request, 'reader') and request.reader is not None,
        'reader': getattr(request, 'reader', None)
    }
    return render(request, 'story/home.html', context)


@reader_login_required
def dashboard(request):
    """User dashboard showing current stats and progress"""
    reader = request.reader
    recent_progress = UserProgress.objects.filter(reader=reader)[:5]

    context = {
        'reader': reader,
        'recent_progress': recent_progress,
        'can_continue': reader.current_chapter is not None,
    }
    return render(request, 'story/dashboard.html', context)


@reader_login_required
def chapter_detail(request, chapter_id=None):
    """Display current chapter and available choices"""
    reader = request.reader

    if chapter_id:
        chapter = get_object_or_404(Chapter, id=chapter_id)
    else:
        chapter = reader.current_chapter
        if not chapter:
            chapter = Chapter.objects.first()
            if chapter:
                reader.current_chapter = chapter
                reader.save()
            else:
                messages.error(request, "No chapters available.")
                return redirect('story:dashboard')

    # Get available choices
    available_choices = chapter.get_available_choices(reader)
    unavailable_choices = [choice for choice in chapter.get_choices()
                           if choice not in available_choices]

    context = {
        'chapter': chapter,
        'available_choices': available_choices,
        'unavailable_choices': unavailable_choices,
        'reader': reader,
        'is_terminal': chapter.is_terminal,
    }

    return render(request, 'story/chapter_detail.html', context)


@reader_login_required
@require_POST
def make_choice(request):
    """Handle user's choice selection"""
    try:
        choice_id = request.POST.get('choice_id')
        choice = get_object_or_404(Choice, id=choice_id)
        reader = request.reader

        # Verify reader can make this choice
        if not reader.can_make_choice(choice):
            messages.error(request, "You don't have enough resources for this choice.")
            return redirect('story:chapter_detail')

        # Verify the choice is from the current chapter
        if reader.current_chapter != choice.from_chapter:
            messages.error(request, "Invalid choice for current chapter.")
            return redirect('story:chapter_detail')

        # Record the choice in progress
        UserProgress.objects.create(
            reader=reader,
            chapter=choice.from_chapter,
            choice_made=choice
        )

        # Apply the choice effects
        old_money = reader.money
        old_energy = reader.energy
        reader.make_choice(choice)

        # Show feedback
        money_change = reader.money - old_money
        energy_change = reader.energy - old_energy

        feedback = []
        if money_change != 0:
            feedback.append(f"Money: {money_change:+d}")
        if energy_change != 0:
            feedback.append(f"Energy: {energy_change:+d}")

        if feedback:
            messages.info(request, f"Choice effects: {', '.join(feedback)}")

        # Check if terminal chapter
        if choice.to_chapter.is_terminal:
            messages.success(request, "Congratulations! You've reached an ending!")
            return redirect('story:ending', chapter_id=choice.to_chapter.id)

        return redirect('story:chapter_detail')

    except Exception as e:
        messages.error(request, f"Error processing choice: {str(e)}")
        return redirect('story:chapter_detail')


@reader_login_required
def ending(request, chapter_id):
    """Display ending chapter"""
    chapter = get_object_or_404(Chapter, id=chapter_id, is_terminal=True)
    reader = request.reader

    context = {
        'chapter': chapter,
        'reader': reader,
        'final_stats': {
            'money': reader.money,
            'energy': reader.energy,
        }
    }

    return render(request, 'story/ending.html', context)


@reader_login_required
def restart_story(request):
    """Reset reader's progress and start over"""
    if request.method == 'POST':
        reader = request.reader
        reader.money = 100
        reader.energy = 100
        reader.current_chapter = Chapter.objects.first()
        reader.save()

        messages.success(request, "Story restarted! Good luck on your new adventure.")
        return redirect('story:chapter_detail')

    return render(request, 'story/restart_confirm.html')


@reader_login_required
def progress_history(request):
    """Show reader's complete progress history"""
    reader = request.reader
    progress = UserProgress.objects.filter(reader=reader)

    context = {
        'progress': progress,
        'reader': reader,
    }

    return render(request, 'story/progress_history.html', context)


# API endpoints
@reader_login_required
def api_reader_stats(request):
    """Return current reader stats as JSON"""
    reader = request.reader
    return JsonResponse({
        'money': reader.money,
        'energy': reader.energy,
        'current_chapter': reader.current_chapter.title if reader.current_chapter else None,
    })
