
from django.urls import path



from .views import altaTarjeta, backupBD, cantidadPedidos, configuracion, credito, cuentasCobrarRango, cuentasPagarRango, editarTarjeta, eliminarTarjeta, graficoClientes, graficoProductos, graficoVentasYear, index, graficoVentas, reportesCompras, comprasRango, reportesCuentasCobrar, reportesCuentasPagar, reportesVentaYear, reportesVentas, ventasRango


urlpatterns = [
    path('', index, name="index"),
    path('graficoVentas/', graficoVentas, name="graficoVentas"),
    path('graficoVentasYear/', graficoVentasYear, name="graficoVentasYear"),
    path('reportesVentaYear/', reportesVentaYear, name="reportesVentaYear"),
    path('configuracion/', configuracion, name="configuracion"),
    path('credito/', credito, name="credito"),
    path('altaTarjeta/', altaTarjeta, name="altaTarjeta"),
    path('editarTarjeta/<id>', editarTarjeta, name="editarTarjeta"),
    path('eliminarTarjeta/<id>', eliminarTarjeta, name="eliminarTarjeta"),
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