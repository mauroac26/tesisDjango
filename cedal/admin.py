from django.contrib import admin
from .models import tarjetaCredito, tarjetaDebito, formaPago
# Register your models here.
admin.site.register(tarjetaCredito)
admin.site.register(tarjetaDebito)
admin.site.register(formaPago)