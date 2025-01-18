from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Account(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)