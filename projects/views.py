from django.shortcuts import render
from projects.models import Project

def projects(request):

    # Request all projects from the db and order them by decreasing importance
    projects = Project.objects.order_by('-importance').all()

    # Render the projects template with the projects list
    return render(request, 'projects.html', {'projects': projects})
