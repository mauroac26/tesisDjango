from django.urls import path
from caja.views import consultaCaja, index, aperturaCaja, cierreCaja

urlpatterns = [
    path('', index, name='caja'),
    path('aperturaCaja', aperturaCaja, name='aperturaCaja'),
    path('cierreCaja', cierreCaja, name='cierreCaja'),
    path('consultaCaja', consultaCaja, name='consultaCaja'),

]