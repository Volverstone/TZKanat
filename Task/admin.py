from django.contrib import admin
from . models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    verbose_name = 'Task'
