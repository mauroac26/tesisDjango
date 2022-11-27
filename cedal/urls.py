
from django.urls import path



from .views import altaTarjeta, backupBD, cantidadPedidos, configuracion, credito, cuentasCobrarRango, cuentasPagarRango, graficoClientes, graficoProductos, index, graficoCompras, reportesCompras, comprasRango, reportesCuentasCobrar, reportesCuentasPagar, reportesVentas, ventasRango


urlpatterns = [
    path('', index, name="index"),
    path('graficoCompras/', graficoCompras, name="graficoCompras"),

    path('configuracion/', configuracion, name="configuracion"),
    path('credito/', credito, name="credito"),
    path('altaTarjeta/', altaTarjeta, name="altaTarjeta"),
    path('graficoProductos/', graficoProductos, name="graficoProductos"),
    path('graficoClientes/', graficoClientes, name="graficoClientes"),
    path('cantidadPedidos/', cantidadPedidos, name="cantidadPedidos"),
    # path('prodVencimiento/', prodVencimiento, name="prodVencimiento"),
    path('reportesCompras/', reportesCompras, name="reportesCompras"),
    path('comprasRango/', comprasRango, name="comprasRango"),
    path('reportesVentas/', reportesVentas, name="reportesVentas"),
    path('ventasRango/', ventasRango, name="ventasRango"),
    path('reportesCuentasPagar/', reportesCuentasPagar, name="reportesCuentasPagar"),
    path('cuentasPagarRango/', cuentasPagarRango, name="cuentasPagarRango"),
    path('reportesCuentasCobrar/', reportesCuentasCobrar, name="reportesCuentasCobrar"),
    path('cuentasCobrarRango/', cuentasCobrarRango, name="cuentasCobrarRango"),
    path('backup/', backupBD, name="backup"),
]