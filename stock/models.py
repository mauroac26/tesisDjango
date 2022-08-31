from tkinter import CASCADE
from django.db import models

from user.models import Users
from producto.models import Producto
# Create your models here.
tipo_Movimiento = [
    ["Compra", "Compra"],
    ["Venta", "Venta"],
    ["Ajuste", "Ajuste"]
]



class stock(models.Model):
    id_movimiento = models.IntegerField()
    tipoMovimiento = models.CharField(max_length=50, choices=tipo_Movimiento, verbose_name="Tipo Movimiento")
    detalle = models.CharField(max_length = 150, verbose_name="Observaciones", null=True, blank=True)
    


class ajusteStock(models.Model):
    fecha = models.DateField()
    detalle = models.CharField(max_length = 150, verbose_name="Observaciones", null=True)
    usuario  = models.ForeignKey(Users, on_delete=models.PROTECT)
    

class detalleAjuste(models.Model):
    id_ajuste = models.ForeignKey(ajusteStock, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    stock_nuevo  = models.IntegerField()

    
    