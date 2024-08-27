from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Task


# * View to list all tasks
def task_list(request):
    tasks = Task.objects.all()  # Fetch all from the database
    context = {"tasks": tasks}  # Prepare context with tasks
    return render(request, "tasks/task_list.html", context)


# * View to create tasks
def task_create(request):
    if request.method == "POST":
        title = request.POST.get("title")  # Get the title from the POST data
        description = request.POST.get(
            "description"
        )  # Get the description from the POST data
        task = Task(title=title, description=description)  # Create a new Task instance
        task.save()  # Save in the database
        return redirect("task_list")  # Redirect to the task list page
    context = {}  # Empty context for the form view
    return render(
        request, "tasks/task_form.html", context
    )  # Render form for creating a new task


# * View To Update an existing task
def task_update(request, id):
    task = get_object_or_404(Task, id=id)  # Fetch the task by id
    if request.method == "POST":
        task.title = request.POST.get("title")
        task.description = request.POST.get(
            "description"
        )  # Fixed typo: was 'descripion'
        task.save()  # Save the updated data
        return redirect("task_list")
    context = {"task": task}  # Prepare context with task data
    return render(
        request, "tasks/task_form.html", context
    )  # Render form with existing task data


# * View to delete a task
def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect("task_list")
