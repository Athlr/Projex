from django.urls import path
from projects.views import (
    list_projects,
    show_project,
    create_project,
    all_projects,
    edit_project,
    delete_project,
    view_project,
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", list_projects, name="list_projects"),
    path("all/", all_projects, name="all_projects"),
    path("<int:id>/", show_project, name="show_project"),
    path("view/<int:id>/", view_project, name="view_project"),
    path("create/", create_project, name="create_project"),
    path("edit/<int:id>/", edit_project, name="edit_project"),
    path("delete/<int:id>/", delete_project, name="delete_project"),
]

urlpatterns += staticfiles_urlpatterns()
