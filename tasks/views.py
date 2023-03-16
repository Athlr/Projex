from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm, CompleteForm, NoteForm
from tasks.models import Task, Note


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }

    return render(request, "tasks/create_task.html", context)


@login_required
def edit_task(request, id):
    tasks = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = CompleteForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect("show_my_tasks")
    else:
        form = CompleteForm(instance=tasks)

    context = {
        "tasks_object": tasks,
        "form": form,
    }
    return render(request, "tasks/edit_task.html", context)


@login_required
def edit_whole_task(request, id):
    tasks = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect("show_project", tasks.project.id)
    else:
        form = TaskForm(instance=tasks)

    context = {
        "tasks_object": tasks,
        "form": form,
    }
    return render(request, "tasks/edit_whole_task.html", context)


@login_required
def show_my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "tasks_object": tasks,
    }
    return render(request, "tasks/my_tasks.html", context)


@login_required
def delete_task(request, id):
    tasks = Task.objects.get(id=id)
    tasks.delete()
    return redirect("show_project", tasks.project.id)


@login_required
def show_notes(request, id):
    tasks = Task.objects.filter(id=id)
    notes = Note.objects.filter(task__id=id)
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.task = tasks.first()
            note.save()
            return redirect("show_notes", id)
    else:
        form = NoteForm()
    context = {
        "notes": notes,
        "form": form,
        "tasks": tasks,
    }
    return render(request, "tasks/notes.html", context)


@login_required
def edit_notes(request, id):
    notes = get_object_or_404(Note, id=id)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=notes)
        if form.is_valid():
            form.save()
            return redirect("edit_notes", id)
    else:
        form = NoteForm(instance=notes)
    context = {
        "notes": notes,
        "form": form,
    }
    return render(request, "tasks/edit_notes.html", context)


@login_required
def delete_notes(request, id):
    notes = Note.objects.get(id=id)
    notes.delete()
    return redirect("show_notes", notes.task.id)
