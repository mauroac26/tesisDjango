from django.urls import path
from caja.views import index

urlpatterns = [
    path('', index, name='caja'),
    # path('ingresoDinero/', ingresoDinero, name="ingresoDinero"),

]