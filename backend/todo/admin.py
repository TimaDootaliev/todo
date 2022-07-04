from django.contrib import admin
from .models import ToDo


@admin.register(ToDo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
    prepopulated_fields = {'slug': ('title',)}