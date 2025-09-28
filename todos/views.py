from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.filters import OrderingFilter

# GET /api/todos/ and POST /api/todos/
class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ["created_at", "title", "done"]   # allowed fields
    ordering = ["-created_at"]                          # default fallback (optional)

# GET, PATCH, DELETE /api/todos/<id>/
class TodoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
