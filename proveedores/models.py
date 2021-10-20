from django.db import models

# Create your models here.

opciones_condicion =[
    [0, "Consumidor final"],
    [1, "Responsable inscripto"]
]

class proveedores(models.Model):
    cuit = models.CharField(max_length=12, primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    mail = models.EmailField()
    condicion = models.IntegerField(choices=opciones_condicion)

def __str__(self):
    return self.cuit
