# story/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Chapter, Choice, ReaderUser
from .forms import ReaderUserCreationForm, LoginForm


class SignUpView(CreateView):
    model = ReaderUser
    form_class = ReaderUserCreationForm
    template_name = 'story/signup.html'
    success_url = reverse_lazy('story:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Account created successfully! Please log in.')
        return response


def login_view(request):
    if request.user.is_authenticated:
        return redirect('story:current_chapter')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                # If user doesn't have a current chapter, set to starting chapter
                if not user.current_chapter:
                    starting_chapter = Chapter.objects.filter(is_starting_chapter=True).first()
                    if starting_chapter:
                        user.current_chapter = starting_chapter
                        user.save()

                return redirect('story:current_chapter')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'story/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('story:login')


@login_required
def current_chapter_view(request):
    user = request.user

    # If user doesn't have a current chapter, redirect to start
    if not user.current_chapter:
        return redirect('story:start_adventure')

    chapter = user.current_chapter
    available_choices = chapter.get_available_choices(user)

    context = {
        'chapter': chapter,
        'choices': available_choices,
        'user_stats': {
            'money': user.money,
            'energy': user.energy
        },
        'is_terminal': chapter.is_terminal
    }

    return render(request, 'story/chapter.html', context)


@login_required
def make_choice_view(request, choice_id):
    if request.method == 'POST':
        user = request.user
        choice = get_object_or_404(Choice, id=choice_id)

        # Verify that the choice is from the user's current chapter
        if user.current_chapter != choice.from_chapter:
            messages.error(request, 'Invalid choice for current chapter.')
            return redirect('story:current_chapter')

        # Make the choice
        if user.make_choice(choice):
            # Show cost/gain feedback
            if choice.money_cost < 0:
                messages.info(request, f'You spent {abs(choice.money_cost)} money.')
            elif choice.money_cost > 0:
                messages.success(request, f'You gained {choice.money_cost} money!')

            if choice.energy_cost < 0:
                messages.info(request, f'You spent {abs(choice.energy_cost)} energy.')
            elif choice.energy_cost > 0:
                messages.success(request, f'You gained {choice.energy_cost} energy!')
        else:
            messages.error(request, 'You don\'t have enough resources for this choice.')

        return redirect('story:current_chapter')

    return redirect('story:current_chapter')


@login_required
def start_adventure_view(request):
    user = request.user

    if request.method == 'POST':
        user.reset_adventure()
        messages.success(request, 'Adventure started! Good luck!')
        return redirect('story:current_chapter')

    starting_chapter = Chapter.objects.filter(is_starting_chapter=True).first()

    if not starting_chapter:
        messages.error(request, 'No starting chapter found. Please contact the administrator.')
        return redirect('story:profile')

    context = {
        'starting_chapter': starting_chapter,
        'has_current_adventure': user.current_chapter is not None
    }

    return render(request, 'story/start_adventure.html', context)


@login_required
def profile_view(request):
    user = request.user
    history = user.choice_history.all()[:10]  # Last 10 choices

    context = {
        'user': user,
        'history': history,
        'stats': {
            'money': user.money,
            'energy': user.energy,
            'current_chapter': user.current_chapter,
            'choices_made': user.choice_history.count()
        }
    }

    return render(request, 'story/profile.html', context)


@login_required
def reset_adventure_view(request):
    if request.method == 'POST':
        request.user.reset_adventure()
        messages.success(request, 'Your adventure has been reset!')
        return redirect('story:current_chapter')

    return render(request, 'story/reset_confirm.html')


# API endpoint for AJAX stats update
@login_required
def get_user_stats(request):
    user = request.user
    return JsonResponse({
        'money': user.money,
        'energy': user.energy,
        'current_chapter': user.current_chapter.title if user.current_chapter else None
    })
