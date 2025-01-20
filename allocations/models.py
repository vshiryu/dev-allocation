from django.db import models
from projects.models import Project
from programmers.models import Programmer 
from django.core.exceptions import ValidationError

class Allocation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)
    hours = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.programmer.name} allocated to {self.project.name} for {self.hours} hours'
