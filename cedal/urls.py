from django.urls import path
from .views import index, graficoCompras

urlpatterns = [
    path('', index, name="index"),
    path('graficoCompras/', graficoCompras, name="graficoCompras"),

]