from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = None
    is_security = models.BooleanField(default=False)
    is_senate = models.BooleanField(default=False)
    is_sdc = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 
    objects = CustomUserManager()

    def __str__(self):
        return self.email

