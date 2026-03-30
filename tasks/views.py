from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages

from .models import Task
from .forms import CustomUserCreationForm, TaskForm
from .services import TaskService


def signup(request):
    if request.user.is_authenticated:
        return redirect('task_list')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Bem-vindo, {user.username}! Conta criada com sucesso.')
            return redirect('task_list')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


@login_required
def task_list(request):
    status_filter = request.GET.get('filter', 'all')
    valid_filters = {'all', 'pending', 'completed'}
    if status_filter not in valid_filters:
        status_filter = 'all'

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            TaskService.create_task(
                user=request.user,
                title=form.cleaned_data['title'],
                priority=form.cleaned_data['priority'],
                deadline=form.cleaned_data.get('deadline'),
            )
            messages.success(request, 'Tarefa criada com sucesso!')
            return redirect(f'/?filter={status_filter}')
        else:
            messages.error(request, 'Verifique os campos e tente novamente.')
    else:
        form = TaskForm()

    tasks = TaskService.get_user_tasks(request.user, status_filter)

    counts = {
        'all': Task.objects.filter(user=request.user).count(),
        'pending': Task.objects.filter(user=request.user, completed=False).count(),
        'completed': Task.objects.filter(user=request.user, completed=True).count(),
    }

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'form': form,
        'current_filter': status_filter,
        'counts': counts,
    })


@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            TaskService.update_task(
                task=task,
                title=form.cleaned_data['title'],
                priority=form.cleaned_data['priority'],
                deadline=form.cleaned_data.get('deadline'),
            )
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('task_list')
        else:
            messages.error(request, 'Verifique os campos e tente novamente.')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})


@login_required
def toggle_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    TaskService.toggle_task(task)

    if task.completed:
        messages.success(request, f'"{task.title}" marcada como concluída.')
    else:
        messages.info(request, f'"{task.title}" reaberta.')

    return redirect(request.META.get('HTTP_REFERER', 'task_list'))


@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == 'POST':
        title = task.title
        TaskService.delete_task(task)
        messages.warning(request, f'Tarefa "{title}" removida.')

    return redirect('task_list')
