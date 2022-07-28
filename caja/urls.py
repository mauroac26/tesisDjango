from django.urls import path
from caja.views import index, aperturaCaja, cierreCaja

urlpatterns = [
    path('', index, name='caja'),
    path('aperturaCaja', aperturaCaja, name='aperturaCaja'),
    path('cierreCaja', cierreCaja, name='cierreCaja'),

]