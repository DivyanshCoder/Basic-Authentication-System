from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class UserProfile(AbstractUser):
#     username = models.CharField(max_length=150, unique=True)
#     email = models.CharField(max_length=254, unique=True)
#     password = models.CharField(max_length=128)
#     date_joined = models.DateTimeField(auto_now_add=True)   

#     def __str__(self):
#         return self.username    