from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Task
from .forms import ProjectForm, TaskForm

def index(request):
    return render(request, 'project_management_tool/index.html')

def register(request):
    # Registration logic here
    pass

def login(request):
    # Login logic here
    pass

@login_required
def dashboard(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'project_management_tool/dashboard.html', {'projects': projects})

@login_required
def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.user != project.owner:
        return redirect('dashboard')
    return render(request, 'project_management_tool/project_detail.html', {'project': project})

@login_required
def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.user != task.project.owner:
        return redirect('dashboard')
    return render(request, 'project_management_tool/task_detail.html', {'task': task})

@login_required
def new_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'project_management_tool/new_project.html', {'form': form})

@login_required
def new_task(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = TaskForm()
    return render(request, 'project_management_tool/new_task.html', {'form': form, 'project': project})