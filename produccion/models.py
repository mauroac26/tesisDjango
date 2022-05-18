from producto.models import Producto
from django.db import models
from user.models import Users
# Create your models here.

class Produccion(models.Model):
    fecha = models.DateField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False, verbose_name="Cantidad")
    usuario = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __int__(self):
        return self.id

estado = [
    ['Pendiente', 'Pendiente'],
    ['Producido', 'Producido']
]

class Pedido(models.Model):
    fecha = models.DateField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False, verbose_name="Cantidad")
    estado = models.CharField(choices=estado, verbose_name="Estado", max_length = 50)

    def __int__(self):
        return self.id
    