from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)

    deadline = models.DateTimeField(null=True, blank=True)   # 🔥 yangi
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title