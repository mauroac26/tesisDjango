from django.urls import path
from proveedores.views import eliminarProveedor, index, altaProveedor, editarProveedor

urlpatterns = [
    path('', index, name="proveedores"),
    path('altaProveedor/', altaProveedor, name="altaProveedor"),
    path('editarProveedor/<id>', editarProveedor, name="editarProveedor"),
    path('eliminarProveedor/<id>', eliminarProveedor, name="eliminarProveedor"),

]