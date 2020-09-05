from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

def index(request):
    todo = Todo.objects.all()

    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'todo':todo, 'form':form}
    return render(request, 'todo/list.html', context)


def updateTask(request, key):
    task = Todo.objects.get(id=key)

    form = TodoForm(instance=task)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}

    return render(request, 'todo/update_task.html', context)

def delete_task(request, key):
    obj = Todo.objects.get(id=key)

    if request.method == 'POST':
        obj.delete()
        return redirect('/')

    context = {'obj':obj}
    return render(request, 'todo/delete.html', context)