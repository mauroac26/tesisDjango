from django.contrib import admin
from compras.models import Compras, detalleCompra

# Register your models here.

class detalleCompraAdmin(admin.ModelAdmin):
    list_display = ["id_compra", "id_producto", "cantidad", "iva", "subTotal", "total"]
    #list_per_page = 5

class CompraAdmin(admin.ModelAdmin):
    list_display = ["id", "comprobante", "fecha"]
    list_filter = ["fecha"]

admin.site.register(Compras, CompraAdmin)
admin.site.register(detalleCompra, detalleCompraAdmin)