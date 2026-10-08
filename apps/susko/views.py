from django.shortcuts import render

from .models import Section


def susko(request):
    """Render the single Šuško page: a main section and the ones below it."""
    context = {
        "main_section": Section.objects.main_section(),
        "sections": Section.objects.other_sections(),
    }

    return render(request, "susko/susko.html", context)
