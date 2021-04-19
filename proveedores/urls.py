from django.urls import path
from proveedores.views import index, altaProveedor

urlpatterns = [
    path('', index, name="proveedores"),
    path('altaProveedor/', altaProveedor, name="altaProveedor"),

]