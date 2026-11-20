from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, "portfolio_site/home.html", {"projects": projects})