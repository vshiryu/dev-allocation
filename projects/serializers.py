from rest_framework import serializers
from .models import Project
from technologies.models import Technology

class ProjectSerializer(serializers.ModelSerializer):
    technologies = serializers.PrimaryKeyRelatedField(queryset=Technology.objects.all(), many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'start_date', 'end_date', 'technologies']

    def validate(self, attrs):
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')
        if (start_date > end_date):
            raise serializers.ValidationError("Start date cannot be after End date")

        return attrs