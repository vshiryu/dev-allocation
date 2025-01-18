from rest_framework import serializers
from .models import Project
from technologies.models import Technology

class ProjectSerializer(serializers.ModelSerializer):
    technologies = serializers.PrimaryKeyRelatedField(queryset=Technology.objects.all(), many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'start_date', 'end_date', 'technologies']
