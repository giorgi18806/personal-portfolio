from django.shortcuts import render

from .models import Project


def home(request):
    context = {
        'projects': Project.objects.all(),
    }
    return render(request, 'portfolio/home.html', context)
