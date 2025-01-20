from django.db import models
from technologies.models import Technology

class Programmer(models.Model):
    name = models.CharField(max_length=255)
    technologies = models.ManyToManyField(Technology)

    def __str__(self):
        return self.name
