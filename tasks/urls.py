from django.urls import path
from tasks.views import (
    create_task,
    show_my_tasks,
    edit_task,
    show_notes,
    edit_notes,
    delete_notes,
    edit_whole_task,
    delete_task,
)

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", show_my_tasks, name="show_my_tasks"),
    path("edit/<int:id>/", edit_task, name="edit_task"),
    path("edit-whole/<int:id>/", edit_whole_task, name="edit_whole_task"),
    path("delete/<int:id>/", delete_task, name="delete_task"),
    path("notes/<int:id>/", show_notes, name="show_notes"),
    path("notes/edit/<int:id>/", edit_notes, name="edit_notes"),
    path("notes/delete/<int:id>/", delete_notes, name="delete_notes"),
]
