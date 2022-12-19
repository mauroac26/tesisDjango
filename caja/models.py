
from django.db import models
from datetime import datetime
from django.utils import timezone

from base.models import BaseModel
# Create your models here.


opciones_mov = [
    [0, "Ingreso"],
    [1, "Egreso"],
]

class Caja(BaseModel):
    nombre = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Caja'
        verbose_name_plural = 'Cajas'

    def __str__(self):
        return str(self.id)


class movCaja(BaseModel):
    fecha = models.DateTimeField()
    descripcion = models.CharField(max_length=50)
    operacion = models.IntegerField(choices=opciones_mov, default=0)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    saldo = models.DecimalField(max_digits=8, decimal_places=2)
    id_caja = models.ForeignKey(Caja, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Movimiento de Caja'
        verbose_name_plural = 'Movimientos de cajas'

    def __int__(self):
        return self.id