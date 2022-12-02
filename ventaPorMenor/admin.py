from django.contrib import admin
from .models import DetalleventaPorMenor, ventaPorMenor
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.

admin.site.register(ventaPorMenor, SimpleHistoryAdmin)
admin.site.register(DetalleventaPorMenor, SimpleHistoryAdmin)
