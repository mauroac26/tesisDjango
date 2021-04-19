from django.urls import path
from compras.views import index, altaCompra, productoAutocomplete

urlpatterns = [
    path('', index, name='compras'),
    path('altaCompra/', altaCompra, name="altaCompra"),
    path('productoAutocomplete/', productoAutocomplete, name="productoAutocomplete"),

]