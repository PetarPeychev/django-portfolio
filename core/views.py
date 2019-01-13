from django.shortcuts import render
from projects.models import Project

def index(request):

    # Request the 3 most important projects from the DB
    projects = Project.objects.order_by('-importance').all()[0:3]

    # Render the index page with the 3 projects
    return render(request, 'index.html', {'projects': projects})
