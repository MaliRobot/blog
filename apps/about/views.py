from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .forms import ContactForm
from .models import About, Contact

# Create your views here.


def about(request):
    about = About.objects.get(pk=1)
    template = loader.get_template("about.html")
    context = {"about": about}

    if request.method == "POST":
        form = ContactForm(request.POST)
        is_valid = form.is_valid()

        print("CONTACT POST received")
        print("CONTACT form valid:", is_valid)
        print("CONTACT form errors:", form.errors)

        if is_valid:
            message = Contact(
                subject=form.cleaned_data["subject"],
                message=form.cleaned_data["message"],
                email=form.cleaned_data["email"],
            )
            message.save()
            print("CONTACT saved, pk:", message.pk)
            return render(
                request,
                "about.html",
                {"form": None, "submitted": True, "about": about},
            )

    form = ContactForm()
    context["form"] = form

    return HttpResponse(template.render(context, request))
