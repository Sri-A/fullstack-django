from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.list_todos, name='lost_todos'),
    path('todos/create', views.create_todo, name='create_todo'),
]