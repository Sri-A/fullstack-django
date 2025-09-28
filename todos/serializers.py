from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'done', 'created_at']
    
    def validate_title(self, value: str) -> str:
        # Normalize whitespace
        value = (value or "").strip()
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters.")
        return value
