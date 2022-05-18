from django.contrib import admin

# Register your models here.
from .models import Pedido, Produccion
# Register your models here.

admin.site.register(Produccion)
admin.site.register(Pedido)