from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect

from django.views import View

from .models import Task
from .forms import TaskForm

# Create your views here.
class MainPageView(View):
    """ to list all tasks and create a new task"""
    
    def get(self, request):
        """ to list all completed tasks present in the db"""
        tasks_list = Task.objects.filter(is_complete=False)
        context = {
            "form": TaskForm(),
            "tasks_list": tasks_list,
            "error_mssg": "",
        }
        return render(request, "coreapp/mainpage.html", context)
    
    def post(self, request):
        """ to create a new task in the db"""
        submitted_taskform = TaskForm(request.POST or None)  
        if submitted_taskform.is_valid():
            new_todo = submitted_taskform.cleaned_data['title']
            if Task.objects.filter(title=new_todo).exists():
                error_mssg = "You already have added this to your list"
                form = submitted_taskform
            else:
                error_mssg = ""
                form = TaskForm()
                submitted_taskform.save()
            context = {
                "form": form,
                "tasks_list": Task.objects.filter(is_complete=False),
                "error_mssg": error_mssg,
            }
            return render(request, "coreapp/mainpage.html", context)
        else:
            return render(request, "coreapp/mainpage.html", {"form": submitted_taskform})
       
      
    
class EditTaskView(View):
    """ to edit a task"""
    
    def get(self, request, id):
        """ to display task that is to be edited"""
        task = Task.objects.get(pk=id)
        tasks_list = Task.objects.filter(is_complete=False).exclude(id=id)
        task_form = TaskForm({"title": task.title, "is_important": task.is_important})
        context = {
            "form": task_form,
            "tasks_list": tasks_list,
            "id": id,
            "error_mssg": ""
        }
        return render(request, "coreapp/edittask.html", context)

    def post(self, request, id):
        """ updates the task title field and is_important field """
        edited_taskform = TaskForm(request.POST)
        if edited_taskform.is_valid():
            new_task_title = edited_taskform.cleaned_data.get('title')
            new_task_imp = edited_taskform.cleaned_data.get('is_important')  
            tasks_list = Task.objects.filter(is_complete=False)    
            if Task.objects.filter(title=new_task_title).exists():
                """ checks if the updated task is already present in the db"""
                task = Task.objects.get(id=id)
                if task.is_important == new_task_imp:
                    error_mssg = "You already have added this to your list"
                    context = {
                        "form": edited_taskform,
                        "tasks_list": tasks_list,
                        "error_mssg": error_mssg,
                        "id": id
                    }
                    return render(request,"coreapp/edittask.html", context)
           
            task = Task.objects.get(id=id) 
            task.title =  new_task_title
            task.is_important = new_task_imp
            task.save()
            return redirect('coreapp:main-page')
        else:
            tasks_list = Task.objects.filter(is_complete=False)
            context = {
            "form": edited_taskform,
            "tasks_list": tasks_list,
            "id": id,
            "error_mssg": ""
            }
            return render(request,"coreapp/edittask.html", context)

    
def ImportantTasksView(request):
    """ to list all incomplete important tasks """
    if request.method == 'GET':
        form = TaskForm()
        tasks_list = Task.objects.filter(is_important=1) & Task.objects.filter(is_complete=False) 
        context = {
            "form": form,
            "tasks_list": tasks_list
        }
        return render(request, 'coreapp/importanttasks.html', context)
    
    
def CompletedTasksView(request):
    """ to list all completed tasks"""
    tasks_list = Task.objects.filter(is_complete=1)
    context = {
            "form": TaskForm(),
            "tasks_list": tasks_list
    }
    return render(request, 'coreapp/completedtasks.html', context)
    
        
def DoneTaskView(request, id):
    """ to mark a task as completed"""
    task = Task.objects.get(id=id)
    task.is_complete = True
    task.save()
    return redirect('coreapp:main-page')


def DeleteTaskView(request, id):
    """ to delete a task"""
    Task.objects.get(id=id).delete()
    return redirect('coreapp:completed-tasks')


def IncompleteTaskView(request, id):
    """ to mark a task as incomplete"""
    task = Task.objects.get(id=id)
    task.is_complete = False
    task.save()
    return redirect('coreapp:main-page')