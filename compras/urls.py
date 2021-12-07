from django.urls import path
from compras.views import imprimir, index, altaCompra, productoAutocomplete, proveedorAutocomplete, cargarCompra, prueba, cargarDetalleCompra, detallesCompra, reporteCompras

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
    
]