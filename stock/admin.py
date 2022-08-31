from django.contrib import admin
from .models import ajusteStock, detalleAjuste, stock
# Register your models here.
admin.site.register(stock)
admin.site.register(ajusteStock)
admin.site.register(detalleAjuste)