from django.contrib import admin
from .models import Todo

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "done", "created_at")
    list_filter = ("done",)
    search_fields = ("title",)

