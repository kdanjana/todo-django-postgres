MainPageView::
get:    gets all in completed tasks from the db and display them on MainPageView
post:   add new task, task item entered in the TaskForm() is collected 
        checks if the entered taskform is valid or not , then checks if the entered task is already
        present in the db, if the task is already present and that task is incomeplete(is_complete=False)
        send the page with an error message

EditTaskView::
get:   checks if the id exists in the db , if id exists then that id's title is retirved and displayed
        if id doesnt exist in the db then page is displayed with an error message
post:  the newly edited task is collected and we will check if task is valid or not, then check if the
        task is already present and that task is incomeplete(is_complete=False) in the db


ImportantTasksView:
get:  get all the tasks that are important(is_important=True) , but not comlpete(is_complete=False)


CompletedTasksView:
get : get all the tasks that are completed(is_complete=True)

DoneTaskView:
to mark that task as completed(is_complete=true)


DeletTaskView:
to delete task from the db

IncompleteTaskView:
to mark task as incomplete (is_complete=false)



jpeg-dev zlib zlib-dev                               --- needed for pillows
build-base postgresql-dev musl-dev  postgresql-client --- needed for postgres db

--access-logfile=- --error-logfile=- --> to watch logs in the console

