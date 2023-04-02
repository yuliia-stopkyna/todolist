from django.urls import path

from tasks.views import (
    TaskListView,
    TaskCreateView,
    TagListView,
    TagCreateView,
    TagDeleteView,
    TagUpdateView,
    TaskUpdateStatusView,
)

app_name = "tasks"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path(
        "tasks/<int:pk>/update_status/",
        TaskUpdateStatusView.as_view(),
        name="task-update-status",
    ),
]
