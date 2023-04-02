from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from tasks.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    template_name = "tasks/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TaskUpdateStatusView(generic.UpdateView):
    model = Task
    fields = ("is_done",)

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect:
        task = self.get_object()
        if task.is_done:
            task.is_done = False
            task.save()
        else:
            task.is_done = True
            task.save()
        return HttpResponseRedirect(reverse("tasks:task-list"))
