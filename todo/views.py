from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from . models import Task

def addTask(request):
    task = request.POST.get("task", "").strip()
    if not task:
        messages.error(request, "Task cannot be empty.")
        return redirect("home")
    
    Task.objects.create(task=task)
    return redirect('home')

def markCompleted(request):
    id = request.POST['task_id']
    task = get_object_or_404(Task,pk = id)
    task.is_completed = True
    task.save()
    return redirect('home')

def deleteTask(request,pk):
    task = get_object_or_404(Task,pk = pk)
    task.is_deleted = True
    task.save()
    return redirect('home')

def restoreTask(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def editTask(request):
    task_id = request.POST.get("task_id")
    task_desc = request.POST.get("task", "").strip()

    if not task_desc:
        messages.error(request, "Task cannot be empty.")
        return redirect("home")
    
    task = get_object_or_404(Task,pk=task_id)
    task.task = task_desc
    task.save()
    return redirect('home')