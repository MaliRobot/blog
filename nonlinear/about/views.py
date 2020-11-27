from django.shortcuts import render
from .models import About, Contact
from django.http import HttpResponse
from django.template import loader
from .forms import ContactForm

# Create your views here.


def about(request):
    about = About.objects.get(pk=1)
    template = loader.get_template('about.html')
    context = {'about': about}

    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form.errors)
        if form.is_valid():
            message = Contact(subject=form.data['subject'], message=form.data['message'], email=form.data['email'])
            message.save()
            return render(request, 'about.html', {'form': None, 'submitted': True, 'about': about})

    form = ContactForm()
    context['form'] = form

    return HttpResponse(template.render(context, request))
