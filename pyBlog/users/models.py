from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='static/images', blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    second_name = models.CharField(max_length=100, blank=True, null=True)
    about = models.TextField(blank=True)


