from django.urls import path
from .views import index, marcas, categorias, altaCategorias, altaMarcas, altaProducto

urlpatterns = [
    path('', index, name="productos"),
    path('marcas/', marcas, name="marcas"),
    path('categorias/', categorias, name="categorias"),
    path('altaCategorias/', altaCategorias, name="altaCategorias"),
    path('altaMarcas/', altaMarcas, name="altaMarcas"),
    path('altaProducto/', altaProducto, name="altaProducto"),
   

]