from django import forms
from django.forms import ModelForm
from tasks.models import Task, Note

# from projects.models import Project
# from django.contrib.auth.models import User


class TaskForm(ModelForm):
    # project = forms.ModelChoiceField(
    #     queryset=Project.objects.all(),
    #     widget=forms.Select(attrs={"class": "form-control"}),
    # )
    # assignee = forms.ModelChoiceField(
    #     queryset=User.objects.all(),
    #     widget=forms.Select(attrs={"class": "form-control"}),
    # )

    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "start_date",
            "due_date",
            "project",
            "assignee",
        )
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "start_date": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                }
            ),
            "due_date": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                }
            ),
            "project": forms.Select(attrs={"class": "form-select"}),
            "assignee": forms.Select(attrs={"class": "form-select"}),
        }


class CompleteForm(ModelForm):
    class Meta:
        model = Task
        fields = ("is_completed",)
        widgets = {
            "is_completed": forms.CheckboxInput(
                attrs={"class": "form-check form-check-inline"}
            )
        }


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = (
            "title",
            "content",
        )
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control note-width mx-auto mt-2"}
            ),
            "content": forms.Textarea(
                attrs={"class": "form-control note-width mx-auto mt-2"}
            ),
        }
