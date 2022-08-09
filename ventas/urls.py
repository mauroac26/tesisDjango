from django.urls import path
from ventas.views import VentasPdf, altaVenta, cargarDetalleVenta, cargarVenta, clienteAutocomplete, detallesVenta, index, pagoVenta, productoVentaAutocomplete, reporteVentas

urlpatterns = [
    path('', index, name='ventas'),
    path('altaVenta', altaVenta, name='altaVenta'),
    path('clienteAutocomplete/', clienteAutocomplete, name="clienteAutocomplete"),
    path('productoVentaAutocomplete/', productoVentaAutocomplete, name="productoVentaAutocomplete"),
    path('cargarVenta/', cargarVenta, name="cargarVenta"),
    path('cargarDetalleVenta/', cargarDetalleVenta, name="cargarDetalleVenta"),
    path('detallesVenta/<id>/', detallesVenta, name="detallesVenta"),
    path('reporteVentas/<id>/', reporteVentas, name="reporteVentas"),
    path('pagoVenta/', pagoVenta, name="pagoVenta"),
    path('repVentas/<id>/', VentasPdf.as_view(), name="repVentas"),
]