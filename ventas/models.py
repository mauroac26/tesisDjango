from django.db import models
from clientes.models import Clientes
from producto.models import Producto
# Create your models here.

tipo_Comprobante = [
    ["Factura", "Factura"],
    ["Recibo", "Recibo"],
    ["Nota Credito", "Nota Credito"]
]

class Ventas(models.Model):
    comprobante = models.CharField(max_length=50, unique=True)
    cuit = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    fecha = models.DateField()
    tipoComprobante = models.CharField(max_length = 50, choices=tipo_Comprobante, verbose_name="Tipo Comprobante")
    

    class Meta:
        ordering = ('-fecha',)


    def __str__(self):
        return str(self.id)
    


class detalleVenta(models.Model):
    id_venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    iva = models.DecimalField(max_digits=8, decimal_places=2)
    subTotal = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Sub-Total")
    total = models.DecimalField(max_digits=8, decimal_places=2)


    def __str__(self):
        return str(self.id)
