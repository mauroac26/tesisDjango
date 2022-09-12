from django.contrib import admin
from .models import Ventas, detalleVenta, formaPagoVenta, tarjetaCredito
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.

class VentasAdmin(admin.ModelAdmin):
    list_display = ('id', 'cuit', 'comprobante', 'fecha', 'tipoComprobante')

admin.site.register(Ventas, SimpleHistoryAdmin)
admin.site.register(detalleVenta)
admin.site.register(formaPagoVenta)
admin.site.register(tarjetaCredito)
