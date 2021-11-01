from django.urls import path
from .views import configuracion, index, graficoCompras, registro

urlpatterns = [
    path('', index, name="index"),
    path('graficoCompras/', graficoCompras, name="graficoCompras"),
    path('registro/', registro, name="registro"),
    path('configuracion/', configuracion, name="configuracion"),
]