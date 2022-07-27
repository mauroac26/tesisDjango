from django.urls import path
from caja.views import index, aperturaCaja

urlpatterns = [
    path('', index, name='caja'),
    path('aperturaCaja', aperturaCaja, name='aperturaCaja'),

]