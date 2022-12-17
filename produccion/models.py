from base.models import BaseModel
from producto.models import Producto
from django.db import models
from user.models import Users
# Create your models here.

estado = [
    ['Pendiente', 'Pendiente'],
    ['Producido', 'Producido']
]

class Produccion(BaseModel):
    fecha = models.DateField()
    producto_retiro = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True, related_name='producto_retiro')
    cantidad_retiro = models.IntegerField(null=False, verbose_name="Cantidad  Retiro", default=1)
    producto_pedido = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True, related_name='producto_pedido')
    cantidad_pedido = models.IntegerField(null=False, verbose_name="Cantidad Pedido", default=1)
    estado = models.CharField(choices=estado, verbose_name="Estado", max_length = 50, default="Pendiente")
    usuario = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)

    class Meta:
        
        verbose_name = 'Produccion'
        verbose_name_plural = 'Produccion'

    def __int__(self):
        return self.id

# estado = [
#     ['Pendiente', 'Pendiente'],
#     ['Producido', 'Producido']
# ]

# class Pedido(models.Model):
#     fecha = models.DateField()
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     cantidad = models.IntegerField(null=False, verbose_name="Cantidad")
#     estado = models.CharField(choices=estado, verbose_name="Estado", max_length = 50)

#     def __int__(self):
#         return self.id
    