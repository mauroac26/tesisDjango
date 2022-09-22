from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.
from .models import Marca, Categoria, Producto
# Register your models here.

admin.site.register(Producto, SimpleHistoryAdmin)
admin.site.register(Marca)
admin.site.register(Categoria)
