from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        Project,
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    assignee = models.ForeignKey(
        User,
        null=True,
        related_name="tasks",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    task = models.ForeignKey(
        Task,
        related_name="tasks",
        on_delete=models.CASCADE,
    )
