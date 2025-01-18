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
        hours = attrs.get('hours')

        if not any(tech in programmer.technologies.all() for tech in required_technologies):
            raise serializers.ValidationError("Programmer must have at least one technology required by the project.")
        
        start_date = project.start_date
        end_date = project.end_date
        
        duration = (end_date - start_date).days
        if hours > duration * 24:
            raise serializers.ValidationError(f"The hours planned for the project cannot exceed the total available hours between {start_date} and {end_date}.")
        
        return attrs
