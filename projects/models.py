from django.db import models
from technologies.models import Technology

class Project(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    technologies = models.ManyToManyField(Technology)

    def __str__(self):
        return self.name
