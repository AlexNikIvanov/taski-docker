from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serialaizer class."""

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'completed')
