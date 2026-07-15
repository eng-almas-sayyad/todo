from django.contrib import admin
from . models import Task
admin.site.register(Task)

from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','task', 'is_completed', 'is_deleted')
    list_editable = ('task','is_completed', 'is_deleted')