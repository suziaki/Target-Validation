from django.contrib import admin
from .models import Project, Task, UserProfile

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date', 'status')
    search_fields = ('name', 'description')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date', 'status', 'project')
    search_fields = ('name', 'description')
    list_filter = ('project',)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__username', 'role')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(UserProfile, UserProfileAdmin)