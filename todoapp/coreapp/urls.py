from django.urls import path

from . import views


app_name = "coreapp"

urlpatterns = [
    path("", views.MainPageView.as_view(), name='main-page'),
    
    path("edittask/<int:id>", views.EditTaskView.as_view(), name='edit-task'),
    
    path("imptasks/", views.ImportantTasksView, name='imp-tasks'),
    
    path("completedtasks/", views.CompletedTasksView, name='completed-tasks'),
    
    path('deletetask/<int:id>', views.DeleteTaskView, name='delete-task'),
    
    path('donetask/<int:id>', views.DoneTaskView, name='done-task'),
    
    path('incompletetask/<int:id>', views.IncompleteTaskView, name='incomplete-task'),
]
