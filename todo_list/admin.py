from django.contrib import admin
from .models import User, Task


class TaskInline(admin.TabularInline):
    model = Task
    extra = 2

class UserAdmin(admin.ModelAdmin):
    inlines = [TaskInline]


admin.site.register(User, UserAdmin)
