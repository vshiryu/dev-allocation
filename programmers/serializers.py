from rest_framework import serializers
from .models import Programmer
from technologies.models import Technology

class ProgrammerSerializer(serializers.ModelSerializer):
    technologies = serializers.PrimaryKeyRelatedField(queryset=Technology.objects.all(), many=True, required=False)

    class Meta:
        model = Programmer
        fields = ['id', 'name', 'technologies']
