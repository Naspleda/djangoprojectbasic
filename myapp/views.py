from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    title = 'Django Course'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    return render(request, 'about.html')

def hello(request, username):
    return HttpResponse('<h1>Hello %s</h1>' % username)


def projects(request):
    projects = list(Project.objects.values()) #Forma habitual
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request):
    # task = Task.objects.get(id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })