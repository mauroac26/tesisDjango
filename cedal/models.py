from django.db import models
from base.models import BaseModel
from compras.models import Compras
from user.models import Users
from ventas.models import Ventas 
# Create your models here.

class backup(BaseModel):
    fecha = models.DateTimeField()
    usuario  = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="Usuarios")
    archivo  = models.CharField(max_length=100)

    class Meta:
        
        verbose_name = 'Respaldo'
        verbose_name_plural = 'Respaldos'

    def __str__(self):
        return self.archivo




# tipo_Tarjeta = [
#     [0, "Credito"],
#     [1, "Debito"]
# ]

# class tarjetas(models.Model):
#     nombre = models.CharField(max_length=100)
#     tipo = models.IntegerField(choices=tipo_Tarjeta, verbose_name="Tipo Tarjeta") 

# def __str__(self):
#     return self.nombre



