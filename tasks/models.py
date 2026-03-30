from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):

    class Priority(models.TextChoices):
        LOW = 'low', 'Baixa'
        MEDIUM = 'medium', 'Média'
        HIGH = 'high', 'Alta'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.LOW,
    )
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def is_overdue(self):
        if self.deadline and not self.completed:
            return self.deadline < timezone.localdate()
        return False

    def get_priority_label(self):
        return self.get_priority_display()

    def get_priority_badge_class(self):
        classes = {
            self.Priority.LOW: 'badge-priority-low',
            self.Priority.MEDIUM: 'badge-priority-medium',
            self.Priority.HIGH: 'badge-priority-high',
        }
        return classes.get(self.priority, 'badge-priority-low')
