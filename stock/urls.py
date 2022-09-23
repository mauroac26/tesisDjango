from django.urls import path

from stock.views import cargarAjuste, cargarDetalleAjuste, movimientoStock, productoAuto, altaAjuste

urlpatterns = [
    path('altaAjuste/', altaAjuste, name='altaAjuste'),
    path('productoAuto/', productoAuto, name="productoAuto"),
    path('cargarAjuste/', cargarAjuste, name='cargarAjuste'),
    path('cargarDetalleAjuste/', cargarDetalleAjuste, name='cargarDetalleAjuste'),
    path('movimientoStock/', movimientoStock, name='movimientoStock'),
]
