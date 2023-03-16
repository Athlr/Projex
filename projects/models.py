from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    STATUSES = [
        ("Not Started", "Not Started"),
        ("In Progress", "In Progress"),
        ("On Hold", "On Hold"),
    ]

    PRIORITIES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=50,
        choices=STATUSES,
        default="Not Started",
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORITIES,
        default="Medium",
    )
    project_manager = models.ForeignKey(
        User,
        related_name="projects",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.name
