from django.urls import path
from ventas.views import altaVenta, detalleFormaPagoVenta, eliminarPagoVenta, registroPagoVenta, cargarPagoVenta, \
    cargarDetalleVenta, cargarVenta, clienteAutocomplete, detallesVenta, index, pagoVenta, productoVentaAutocomplete, ventaAdeudada, eliminarVenta

urlpatterns = [
    path('', index, name='ventas'),
    path('altaVenta', altaVenta, name='altaVenta'),
    path('clienteAutocomplete/', clienteAutocomplete, name="clienteAutocomplete"),
    path('productoVentaAutocomplete/', productoVentaAutocomplete, name="productoVentaAutocomplete"),
    path('cargarVenta/', cargarVenta, name="cargarVenta"),
    path('cargarDetalleVenta/', cargarDetalleVenta, name="cargarDetalleVenta"),
    path('detallesVenta/<id>/', detallesVenta, name="detallesVenta"),
    # path('reporteVentas/<id>/', reporteVentas, name="reporteVentas"),
    path('pagoVenta/', pagoVenta, name="pagoVenta"),
    path('registroPagoVenta/', registroPagoVenta, name="registroPagoVenta"),
    path('ventaAdeudada/', ventaAdeudada, name="ventaAdeudada"),
    path('cargarPagoVenta/', cargarPagoVenta, name="cargarPagoVenta"),
    # path('repVentas/<id>/', VentasPdf.as_view(), name="repVentas"),
    path('detalleFormaPagoVenta/', detalleFormaPagoVenta, name="detalleFormaPagoVenta"),
    path('eliminarPagoVenta/<id>/', eliminarPagoVenta, name="eliminarPagoVenta"),
    path('eliminarVenta/<id>/', eliminarVenta, name="eliminarVenta"),

]