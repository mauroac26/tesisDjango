from django.urls import path

from ventaPorMenor.views import index, altaPedidoPorMenor, cargarPedidoVenta, cargarDetallePedidoVenta, detallePedidoVenta

urlpatterns = [
    path('', index, name="pedidoVentaPorMenor"),
    path('altaPedidoPorMenor/', altaPedidoPorMenor, name="altaPedidoPorMenor"),
    path('cargarPedidoVenta/', cargarPedidoVenta, name="cargarPedidoVenta"),
    path('cargarDetallePedidoVenta/', cargarDetallePedidoVenta, name="cargarDetallePedidoVenta"),
    path('detallePedidoVenta/', detallePedidoVenta, name="detallePedidoVenta"),

]