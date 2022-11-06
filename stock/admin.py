from django.contrib import admin
from .models import ajusteStock, stock
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.

admin.site.register(stock)
admin.site.register(ajusteStock, SimpleHistoryAdmin)
