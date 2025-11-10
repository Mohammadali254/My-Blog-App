from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    profile_picture = models.ImageField(
        upload_to='profile_pics/', 
        default='profile_pics/default.png',
        blank= True
    )

    def __str__(self):
        return self.username