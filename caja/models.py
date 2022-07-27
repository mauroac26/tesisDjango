
from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.


opciones_mov = [
    [0, "Ingreso"],
    [1, "Egreso"],
]


class movCaja(models.Model):
    fecha = models.DateTimeField()
    descripcion = models.CharField(max_length=50)
    operacion = models.IntegerField(choices=opciones_mov, default=0)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    saldo = models.DecimalField(max_digits=8, decimal_places=2)


def __str__(self):
    return self.fecha