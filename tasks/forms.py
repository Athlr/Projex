from django import forms
from django.forms import ModelForm
from tasks.models import Task
from projects.models import Project
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = "datetime-local"


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
            "start_date",
            "due_date",
            "project",
            "assignee",
        )
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "start_date": DateInput(attrs={"class": "form-control"}),
            "due_date": DateInput(attrs={"class": "form-control"}),
            "project": forms.Select(attrs={"class": "form-control"}),
            "assignee": forms.Select(attrs={"class": "form-control"}),
        }
