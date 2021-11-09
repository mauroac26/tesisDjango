from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import NullBooleanField

from proyectoTesis.settings import MEDIA_URL, STATIC_URL
# Create your models here.

nivel = [
    [0, "Administrador"],
    [1, "Vendedor"]
]
class Users(AbstractUser):
    nivel = models.IntegerField(choices=nivel, null=True)
    imagen = models.ImageField(upload_to='usuarios', null=True, blank=True)

    def get_imagen(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'cedal/img/undraw_profile.svg')
    
    # def has_perm(self, perm, obj = None):
    #     return True

    # def has_module_perms(self, app_label):
    #     return True

    