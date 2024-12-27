from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Register the Task model in the admin site"""

    list_display = ["title", "description", "priority_level", "due_date", "status"]
    list_filter = ["title", "priority_level", "due_date", "status"]
    search_fields = ["title", "description"]


admin.site.register(Task, TaskAdmin)
