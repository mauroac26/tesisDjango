from django.urls import path
from clientes.views import editarCliente, eliminarCliente, index, altaClientes

urlpatterns = [
    path('', index, name='clientes'),
    path('altaClientes/', altaClientes, name="altaClientes"),
    path('editarCliente/<id>', editarCliente, name="editarCliente"),
    path('eliminarCliente/<id>', eliminarCliente, name="eliminarCliente"),
    
]