from django.db import models
from base.models import BaseModel
from proveedores.models import proveedores
from producto.models import Producto
# Create your models here.

tipo_Comprobante = [
    ["Factura", "Factura"],
    ["Recibo", "Recibo"],
    ["Nota Credito", "Nota Credito"]
]

estado = [
    ["Pagado", "Pagado"],
    ["Adeudado", "Adeudado"]
]
class Compras(BaseModel):
    comprobante = models.CharField(max_length=8, unique=True)
    cuit = models.ForeignKey(proveedores, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField()
    tipoComprobante =  models.CharField(max_length = 150, choices=tipo_Comprobante, verbose_name="Tipo Comprobante")
    estado = models.CharField(max_length=150, choices=estado, default='Adeudado')

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ('-fecha',)


def __str__(self):
    return self.id
    


class detalleCompra(models.Model):
    id_compra = models.ForeignKey(Compras, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    iva = models.DecimalField(max_digits=8, decimal_places=2)
    subTotal = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Sub-Total")
    total = models.DecimalField(max_digits=8, decimal_places=2)


def __str__(self):
    return self.id_compra


# class ExcelFileUpload(models.Model):
#     excel = models.FileField(upload_to="excel")

tipo_Pago = [
    ["Efectivo", "Efectivo"],
    ["Transferencia", "Transferencia"],
    ["Cheques", "Cheques"]
]

class formaPagoCompra(models.Model):
    fecha = models.DateField()
    total = models.DecimalField(max_digits=8, decimal_places=2 , null=True, blank=True, verbose_name='Monto')
    tipoPago =  models.CharField(max_length=150, choices=tipo_Pago, verbose_name="Tipo Pago")
    id_compra =  models.ForeignKey(Compras, on_delete=models.CASCADE)
    

def __str__(self):
    return self.id


