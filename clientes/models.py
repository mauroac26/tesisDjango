from django.db import models

# Create your models here.

opciones_condicion =[
    [0, "Consumidor final"],
    [1, "Responsable inscripto"]
]

class Clientes(models.Model):
    cuit = models.CharField(max_length=14, primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name="Razon Social")
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    mail = models.EmailField()
    condicion = models.IntegerField(choices=opciones_condicion)

    def __str__(self):
        return self.cuit