from django.contrib import admin
from .models import Ventas, detalleVenta
# Register your models here.
admin.site.register(Ventas)
admin.site.register(detalleVenta)