from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

nivel = [
    [0, "Administrador"],
    [1, "Vendedor"]
]
class Users(AbstractUser):
    nivel = models.IntegerField(choices=nivel, null=True)