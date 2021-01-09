from django.shortcuts import render
from .models import Project # To display database content on any html files from views.py

# Create your views here.


def home(request):

    projects = Project.objects.all() #Grabs all project objects
    return render(request, 'portfolio/home.html', {'projects': projects})