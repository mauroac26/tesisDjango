from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
from .models import Produccion
# Register your models here.

admin.site.register(Produccion, SimpleHistoryAdmin)
# admin.site.register(Pedido)