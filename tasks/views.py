from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.views.decorators.http import require_POST

from django.utils import timezone

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    today = timezone.now().date()
    
    stats = {
        'total': tasks.count(),
        'completed': tasks.filter(completed=True).count(),
        'overdue': tasks.filter(completed=False, due_date__lt=today).count(),
        'today': tasks.filter(due_date=today, completed=False).count()
    }
    
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'stats': stats  # N'oubliez pas d'envoyer les stats au template
    })

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks:task_list')  # ✅ correction ici
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')  # ✅ correction ici
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:task_list')  # ✅ correction ici
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

@login_required
@require_POST
def toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('tasks:task_list')  # ✅ déjà correct
