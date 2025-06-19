from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Task

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active', 'date_joined',)
    search_fields = ('username', 'email',)
    ordering = ('username',)
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth'),
        }),
    )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'user', 'status', 'priority', 'category', 'due_date', 'created_at')
    list_filter = ('status', 'priority', 'category', 'created_at')
    search_fields = ('task_name', 'description', 'user__username', 'user__email')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Task Information', {
            'fields': ('task_name', 'description', 'user')
        }),
        ('Status & Priority', {
            'fields': ('status', 'priority', 'category')
        }),
        ('Dates', {
            'fields': ('due_date',)
        }),
    )
