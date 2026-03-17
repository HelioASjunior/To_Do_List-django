from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(user=request.user, title=title)
            return redirect('task_list')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def toggle_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('task_list')