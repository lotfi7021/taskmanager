from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_user', 'due_date', 'priority', 'completed')
    list_filter = ('completed', 'priority', 'due_date')
    search_fields = ('title', 'description')
    date_hierarchy = 'due_date'
    
    def get_user(self, obj):
        return obj.user.username
    get_user.short_description = 'User'  # Sets column header