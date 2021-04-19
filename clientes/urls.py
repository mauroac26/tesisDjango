from django.urls import path
from clientes.views import index, altaClientes

urlpatterns = [
    path('', index, name='clientes'),
    path('altaClientes/', altaClientes, name="altaClientes"),

]