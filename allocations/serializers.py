from rest_framework import serializers
from .models import Allocation

class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocation
        fields = ['id', 'project', 'programmer', 'hours']

    def validate(self, attrs):
        project = attrs.get('project')
        programmer = attrs.get('programmer')
        required_technologies = project.technologies.all()

        if not any(tech in programmer.technologies.all() for tech in required_technologies):
            raise serializers.ValidationError("Programmer must have at least one technology required by the project.")
        
        return attrs
