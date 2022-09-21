from django.urls import path
from compras.views import compraAdeudada, detallePago, eliminarCompra, eliminarPago, imprimir, index, altaCompra, productoAutocomplete, proveedorAutocomplete, cargarCompra, prueba, cargarDetalleCompra, detallesCompra, registroPago, reporteCompra, reporteCompras, pago, detalleFormaPago

urlpatterns = [
    path('', index, name='compras'),
    path('altaCompra/', altaCompra, name="altaCompra"),
    path('productoAutocomplete/', productoAutocomplete, name="productoAutocomplete"),
    path('proveedorAutocomplete/', proveedorAutocomplete, name="proveedorAutocomplete"),
    path('cargarCompra/', cargarCompra, name="cargarCompra"),
    path('prueba/', prueba, name="prueba"),
    path('cargarDetalleCompra/', cargarDetalleCompra, name="cargarDetalleCompra"),
    path('detallesCompra/<id>/', detallesCompra, name="detallesCompra"),
    #path('cargarFormaPago/', cargarFormaPago, name="cargarFormaPago"),
    path('imprimir/', imprimir, name="imprimir"),
    path('reporteCompras/', reporteCompras, name="reporteCompras"),
    #path('reporteExcel/', reporteExcel, name="reporteExcel"),
    #path('reporteComprasExcel/', reporteComprasExcel, name="reporteComprasExcel"),
    path('pago/', pago, name="pago"),
    path('registroPago/', registroPago, name="registroPago"),
    path('compraAdeudada/', compraAdeudada, name="compraAdeudada"),
    path('detallePago/', detallePago, name="detallePago"),
    path('reporteCompra/', reporteCompra, name="reporteCompra"),
    path('eliminarCompra/<id>/', eliminarCompra, name="eliminarCompra"),
    path('eliminarPago/<id>/', eliminarPago, name="eliminarPago"),
    path('detalleFormaPago/', detalleFormaPago, name="detalleFormaPago"),
]