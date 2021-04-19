from django.db import models

# Create your models here.
class Categoria(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion


class Marca(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion


class Producto(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    precio_compra = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    precio_venta = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    stock = models.IntegerField()
    stock_min = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre