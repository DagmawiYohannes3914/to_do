from django.shortcuts import render, redirect

from .models import TodoItem
from .forms import TodoForm

# Create your views here.


def index(request):
    todos = TodoItem.objects.all()
    return render(request, 'tasks/index.html', {'todos': todos})


def add_task(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    return render(request, 'tasks/add_task.html', {'form': form})


def delete_task(request, task_id):
    task = TodoItem.objects.get(id=task_id)
    task.delete()
    return redirect('index')


def toggle_task(request, task_id):
    task = TodoItem.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('index')
