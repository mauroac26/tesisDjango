from django.db import models
from compras.models import Compras 
# Create your models here.


class tarjetaDebito(models.Model):
    nombre = models.CharField(max_length=100)

def __str__(self):
    return self.nombre


class tarjetaCredito(models.Model):
    nombre = models.CharField(max_length=100)

def __str__(self):
    return self.nombre


class formaPago(models.Model):
    efectivo = models.DecimalField(max_digits=8, decimal_places=2 , null=True, blank=True)
    credito = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    debito = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    tipoCredito = models.ForeignKey(tarjetaCredito, on_delete=models.PROTECT, null=True, blank=True)
    tipoDebito = models.ForeignKey(tarjetaDebito, on_delete=models.PROTECT, null=True, blank=True)
    cuotas = models.IntegerField(null=True, blank=True)
    id_compra =  models.ForeignKey(Compras, on_delete=models.CASCADE)

def __str__(self):
    return self.id
