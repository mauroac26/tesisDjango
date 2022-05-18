
from django.urls import path


from .views import altaTarjeta, cantidadPedidos, configuracion, credito, graficoClientes, graficoProductos, index, graficoCompras

urlpatterns = [
    path('', index, name="index"),
    path('graficoCompras/', graficoCompras, name="graficoCompras"),
    #path('usuarios/', usuarios, name="usuarios"),
    path('configuracion/', configuracion, name="configuracion"),
    path('credito/', credito, name="credito"),
    path('altaTarjeta/', altaTarjeta, name="altaTarjeta"),
    path('graficoProductos/', graficoProductos, name="graficoProductos"),
    path('graficoClientes/', graficoClientes, name="graficoClientes"),
    path('cantidadPedidos/', cantidadPedidos, name="cantidadPedidos"),
]