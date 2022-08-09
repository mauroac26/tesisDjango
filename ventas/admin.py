from django.contrib import admin
from .models import Ventas, detalleVenta, formaPagoVenta
# Register your models here.

class VentasAdmin(admin.ModelAdmin):
    list_display = ('id', 'cuit', 'comprobante', 'fecha', 'tipoComprobante')

admin.site.register(Ventas, VentasAdmin)
admin.site.register(detalleVenta)
admin.site.register(formaPagoVenta)