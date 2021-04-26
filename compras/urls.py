from django.urls import path
from compras.views import index, altaCompra, productoAutocomplete, proveedorAutocomplete, cargarCompra, prueba, cargarDetalleCompra

urlpatterns = [
    path('', index, name='compras'),
    path('altaCompra/', altaCompra, name="altaCompra"),
    path('productoAutocomplete/', productoAutocomplete, name="productoAutocomplete"),
    path('proveedorAutocomplete/', proveedorAutocomplete, name="proveedorAutocomplete"),
    path('cargarCompra/', cargarCompra, name="cargarCompra"),
    path('prueba/', prueba, name="prueba"),
    path('cargarDetalleCompra/', cargarDetalleCompra, name="cargarDetalleCompra"),
    
]