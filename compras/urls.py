from django.urls import path
from compras.views import compraAdeudada, detallePago, eliminarCompra, eliminarPago, index, altaCompra, productoAutocomplete, proveedorAutocomplete, cargarCompra, cargarDetalleCompra, detallesCompra, registroPago, reporteCompra, pago, detalleFormaPago

urlpatterns = [
    path('', index, name='compras'),
    path('altaCompra/', altaCompra, name="altaCompra"),
    path('productoAutocomplete/', productoAutocomplete, name="productoAutocomplete"),
    path('proveedorAutocomplete/', proveedorAutocomplete, name="proveedorAutocomplete"),
    path('cargarCompra/', cargarCompra, name="cargarCompra"),
    path('cargarDetalleCompra/', cargarDetalleCompra, name="cargarDetalleCompra"),
    path('detallesCompra/<id>/', detallesCompra, name="detallesCompra"),
    path('pago/', pago, name="pago"),
    path('registroPago/', registroPago, name="registroPago"),
    path('compraAdeudada/', compraAdeudada, name="compraAdeudada"),
    path('detallePago/', detallePago, name="detallePago"),
    path('reporteCompra/', reporteCompra, name="reporteCompra"),
    path('eliminarCompra/<id>/', eliminarCompra, name="eliminarCompra"),
    path('eliminarPago/<id>/', eliminarPago, name="eliminarPago"),
    path('detalleFormaPago/', detalleFormaPago, name="detalleFormaPago"),
]