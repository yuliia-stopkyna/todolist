from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(to=Tag, related_name="tasks")

    class Meta:
        ordering = ("is_done", "-created_at")

    def __str__(self) -> str:
        return self.title
