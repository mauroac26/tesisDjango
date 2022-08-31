from django.urls import path

from stock.views import cargarAjuste, cargarDetalleAjuste, productoAuto, altaAjuste

urlpatterns = [
    path('altaAjuste/', altaAjuste, name='Ajuste'),
    path('productoAuto/', productoAuto, name="productoAuto"),
    path('cargarAjuste/', cargarAjuste, name='cargarAjuste'),
    path('cargarDetalleAjuste/', cargarDetalleAjuste, name='cargarDetalleAjuste'),
]