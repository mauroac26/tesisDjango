from django.contrib import admin
from caja.models import Caja, movCaja
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
admin.site.register(movCaja, SimpleHistoryAdmin)
admin.site.register(Caja, SimpleHistoryAdmin)