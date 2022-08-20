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
    estado = models.CharField(max_length=150, default='Adeudado')

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


class tarjetaDebito(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class tarjetaCredito(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


tipo_Pago = [
    ["Efectivo", "Efectivo"],
    ["Credito", "Credito"],
    ["Debito", "Debito"]
]

class formaPagoVenta(models.Model):
    fecha = models.DateField()
    total = models.DecimalField(max_digits=8, decimal_places=2 , null=True, blank=True, verbose_name='Monto')
    tipoCredito = models.ForeignKey(tarjetaCredito, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Seleccionar Tarjeta')
    tipoPago =  models.CharField(choices=tipo_Pago, verbose_name="Tipo Pago", max_length=150)
    cuotas = models.IntegerField(null=True, blank=True)
    id_venta =  models.ForeignKey(Ventas, on_delete=models.CASCADE, null=True, blank=True)
    

def __str__(self):
    return self.id