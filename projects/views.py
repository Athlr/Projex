from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project
from projects.forms import ProjectForm


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects,
    }
    return render(request, "projects/projects.html", context)


@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        "project_object": project,
    }
    return render(request, "projects/project_detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {
        "form": form,
    }
    return render(request, "projects/create_project.html", context)
