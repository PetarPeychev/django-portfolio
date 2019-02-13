from django.shortcuts import render
from projects.models import Project

def index(request):

    # Request the 3 most important projects from the db
    projects = Project.objects.order_by('-importance').all()[0:3]

    # Render the index template with the 3 projects
    return render(request, 'index.html', {'projects': projects})

def skills(request):

    # Render the skills page
    return render(request, 'skills.html')

def contact(request):

    # Render the skills page
    return render(request, 'contact.html')
