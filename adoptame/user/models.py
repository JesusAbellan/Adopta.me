from django.db import models
from django.contrib.auth.models import AbstractUser

class PetOwner(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    is_shelter = models.BooleanField(default=False)

    def __str__(self):
        return self.username


# Create your models here.