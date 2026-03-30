from .models import Task


class TaskService:

    @staticmethod
    def get_user_tasks(user, status_filter=None):
        queryset = Task.objects.filter(user=user)

        if status_filter == 'pending':
            queryset = queryset.filter(completed=False)
        elif status_filter == 'completed':
            queryset = queryset.filter(completed=True)

        return queryset.order_by(
            'completed',
            '-priority',
            'deadline',
            '-created_at'
        )

    @staticmethod
    def create_task(user, title, priority, deadline=None):
        return Task.objects.create(
            user=user,
            title=title.strip(),
            priority=priority,
            deadline=deadline,
        )

    @staticmethod
    def update_task(task, title, priority, deadline=None):
        task.title = title.strip()
        task.priority = priority
        task.deadline = deadline
        task.save()
        return task

    @staticmethod
    def toggle_task(task):
        task.completed = not task.completed
        task.save()
        return task

    @staticmethod
    def delete_task(task):
        task.delete()

    @staticmethod
    def get_task_or_none(task_id, user):
        try:
            return Task.objects.get(id=task_id, user=user)
        except Task.DoesNotExist:
            return None
