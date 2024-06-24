from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):

    def get_queryset(model):
        return model.objects.all()
    
    class Meta:
        model = Project
        fields = '__all__'
