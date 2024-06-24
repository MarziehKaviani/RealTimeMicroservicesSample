from rest_framework import serializers
from .models import Task, Comment


class TaskSerializer(serializers.ModelSerializer):

    def get_queryset(model):
        return model.objects.all()
    
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('created_at',)
