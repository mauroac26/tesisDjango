from user.models import Users
from datetime import datetime
from django.db import models

from producto.models import Producto
from base.models import BaseModel
# Create your models here.

class stock(models.Model):
    fecha = models.DateTimeField(null=True)
    tipoMovimiento = models.CharField(max_length=50, verbose_name="Tipo Movimiento")
    producto = models.CharField(max_length = 150)
    detalle = models.CharField(max_length = 150, verbose_name="Observaciones", null=True, blank=True)
    cantidad = models.IntegerField()
    stockActual = models.IntegerField()
    usuario  = models.CharField(max_length=150, verbose_name="Usuarios")
    
    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'
        ordering = ('-fecha',)
        # get_latest_by = 'fecha'


motivo = [
    ["Vencido", "Vencido"],
    ["Devolucion", "Devolucion"],
    ["Mal estado", "Mal estado"]
]

class ajusteStock(BaseModel):
    fecha = models.DateTimeField()
    usuario  = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="Usuarios")
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad  = models.IntegerField(default=1)
    motivo = models.CharField(choices=motivo, max_length=150)
    detalle = models.CharField(max_length = 150, verbose_name="Observaciones", null=True)

    class Meta:
        
        verbose_name = 'Ajuste Stock'
        verbose_name_plural = 'Ajustes Stocks'


    def __str__(self):
        return str(self.id)





# class detalleAjuste(models.Model):
#     id_ajuste = models.ForeignKey(ajusteStock, on_delete=models.CASCADE)
#     id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     cantidad  = models.IntegerField(default=1)
#     motivo = models.CharField(choices=motivo, max_length=150)
#     detalle = models.CharField(max_length = 150, verbose_name="Observaciones", null=True)

#     def __str__(self):
#         return str(self.id_ajuste)
    