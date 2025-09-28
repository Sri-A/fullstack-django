from django.urls import path
from .views import TodoListCreateView, TodoRetrieveUpdateDeleteView

urlpatterns = [
    path('todos/', TodoListCreateView.as_view(), name='list_create_todos'),
    path('todos/<int:pk>/', TodoRetrieveUpdateDeleteView.as_view(), name='todo_detail'),
]
