from django.contrib.auth.decorators import login_required
from django.urls import path

from user.views import usuarios
from .views import altaTarjeta, configuracion, credito, graficoProductos, index, graficoCompras

urlpatterns = [
    path('', index, name="index"),
    path('graficoCompras/', graficoCompras, name="graficoCompras"),
    #path('usuarios/', usuarios, name="usuarios"),
    path('configuracion/', configuracion, name="configuracion"),
    path('credito/', credito, name="credito"),
    path('altaTarjeta/', altaTarjeta, name="altaTarjeta"),
    path('graficoProductos/', graficoProductos, name="graficoProductos"),
]