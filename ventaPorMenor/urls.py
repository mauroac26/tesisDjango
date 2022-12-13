from django.urls import path

from ventaPorMenor.views import eliminarVentaMenor, index, altaRetiroPorMenor, cargarRetiroVenta, cargarDetalleRetiroVenta, detalleRetiroVenta

urlpatterns = [
    path('', index, name="retiroVentaPorMenor"),
    path('altaRetiroPorMenor/', altaRetiroPorMenor, name="altaRetiroPorMenor"),
    path('cargarRetiroVenta/', cargarRetiroVenta, name="cargarRetiroVenta"),
    path('cargarDetalleRetiroVenta/', cargarDetalleRetiroVenta, name="cargarDetalleRetiroVenta"),
    path('detalleRetiroVenta/', detalleRetiroVenta, name="detalleRetiroVenta"),
    path('eliminarVentaMenor/<id>', eliminarVentaMenor, name="eliminarVentaMenor"),

]