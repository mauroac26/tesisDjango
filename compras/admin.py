from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from compras.models import Compras, detalleCompra, formaPagoCompra

# Register your models here.

class detalleCompraAdmin(admin.ModelAdmin):
    list_display = ["id_compra", "id_producto", "cantidad", "iva", "subTotal", "total"]
    #list_per_page = 5

class CompraAdmin(SimpleHistoryAdmin):
    list_display = ["id", "comprobante", "fecha"]
    list_filter = ["fecha"]

admin.site.register(Compras, CompraAdmin)
admin.site.register(detalleCompra, detalleCompraAdmin)
admin.site.register(formaPagoCompra)