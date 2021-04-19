from django.contrib import admin
from compras.models import Compras, detalleCompra

# Register your models here.
admin.site.register(Compras)
admin.site.register(detalleCompra)