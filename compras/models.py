from django.db import models
from proveedores.models import proveedores
from producto.models import Producto
# Create your models here.

tipo_Comprbante = [
    [0, "Factura"],
    [1, "Recibo"],
    [2, "Nota Credito"]
]
class Compras(models.Model):
    comprobante = models.CharField(max_length=50)
    cuit = models.ForeignKey(proveedores, on_delete=models.CASCADE)
    fecha = models.DateField()
    iva = models.DecimalField(max_digits=8, decimal_places=2)
    subTotal = models.DecimalField(max_digits=8, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    tipoComprobante = models.IntegerField(choices=tipo_Comprbante)


def __str__(self):
    return self.id


class detalleCompra(models.Model):
    id_compra = models.ForeignKey(Compras, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

def __str__(self):
    return self.id_compra