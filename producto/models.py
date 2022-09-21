from django.db import models

from base.models import BaseModel

# Create your models here.
class Categoria(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion


class Marca(models.Model):
    descripcion = models.CharField(max_length=50)

    class Meta:
        
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.descripcion


class Producto(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    precio_compra = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    precio_venta = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    stock = models.IntegerField()
    stock_min = models.IntegerField(verbose_name='Stock Minimo')
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.SET_NULL)
    marca = models.ForeignKey(Marca, null=True, on_delete=models.SET_NULL)
    vencimiento = models.DateField(null=True)
    

    def __str__(self):
        return self.nombre



    
    
    
    