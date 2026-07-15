from django.shortcuts import render
from django.core.paginator import Paginator
from todo.models import Task

def home(request):
    search_query = request.GET.get('search','')
    
    # tasks = Task.objects.filter(is_completed=False,is_deleted=False).order_by('-updated_at')
    tasks = Task.objects.filter(is_completed=False,is_deleted=False)
    task_count = len(tasks)
    if(search_query):
        tasks = tasks.filter(task__icontains=search_query)
    
   
    #Pagination

    paginator = Paginator(tasks.order_by('-updated_at'),5) #5 Tasks per page
    page_number = request.GET.get('page')
    tasks = paginator.get_page(page_number)

    #################### Completed Task Logic ####################
    search_completed_query = request.GET.get('search_completed','')
    
    completed_tasks = Task.objects.filter(is_completed=True,is_deleted=False)
    complete_task_count = len(completed_tasks)
    if(search_completed_query):
        completed_tasks = completed_tasks.filter(task__icontains=search_completed_query)
    
    #Pagination for Completed Tasks
    
    completed_paginator = Paginator(completed_tasks.order_by('-updated_at'),4)
    completed_page_number = request.GET.get('completed_page')
    completed_tasks = completed_paginator.get_page(completed_page_number)
    
    context = {
        'tasks':tasks,
        'completed_tasks':completed_tasks,
        'task_count':task_count,
        'complete_task_count':complete_task_count,
        'search_completed_query': search_completed_query,
    }
    return render(request,'home.html',context)
