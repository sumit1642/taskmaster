from django.contrib import admin
from .models import Task


# Define a model admin class for Task
class TaskAdmin(admin.ModelAdmin):
    # List of fields to display in the list view
    list_display = ("title", "description", "created_at", "updated_at")

    # Fields to be used for search
    search_fields = ("title", "description")

    # Fields to filter by in the list view
    list_filter = ("created_at", "updated_at")


# Register the Task model with the admin site using the custom TaskAdmin class
admin.site.register(Task, TaskAdmin)
