from django.urls import path

from produccion.views import altaProduccion, eliminarProduccion, index, pedido, producido


urlpatterns = [
    path('', index, name="produccion"),
    path('altaProduccion/', altaProduccion, name="altaProduccion"),
    path('pedido/', pedido, name="pedido"),
    path('producido/', producido, name="producido"),
    path('eliminarProduccion/<id>', eliminarProduccion, name="eliminarProduccion"),
]