import datetime
from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(null=False)
    bio = models.TextField(blank=True, null=True)
    is_critic = models.BooleanField(null=True, blank=False)
    updated_at = models.DateTimeField(default=datetime.datetime.today())

    REQUIRED_FIELDS = ['email', 'birthdate', 'first_name', 'last_name',]