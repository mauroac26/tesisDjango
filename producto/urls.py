from django.urls import path
from .views import editarCategoria, eliminarCategoria, eliminarProducto, index, marcas, categorias, altaCategorias, altaMarcas, altaProducto, editarProducto, editarMarca, eliminarMarca, vencimiento

urlpatterns = [
    path('', index, name="productos"),
    path('marcas/', marcas, name="marcas"),
    path('categorias/', categorias, name="categorias"),
    path('altaCategorias/', altaCategorias, name="altaCategorias"),
    path('altaMarcas/', altaMarcas, name="altaMarcas"),
    path('altaProducto/', altaProducto, name="altaProducto"),
    path('editarProducto/<id>', editarProducto, name="editarProducto"),
    path('eliminarProducto/<id>', eliminarProducto, name="eliminarProducto"),
    path('editarMarca/<id>', editarMarca, name="editarMarca"),
    path('eliminarMarca/<id>', eliminarMarca, name="eliminarMarca"),
    path('editarCategoria/<id>', editarCategoria, name="editarCategoria"),
    path('eliminarCategoria/<id>', eliminarCategoria, name="eliminarCategoria"),
    path('vencimiento/', vencimiento, name="vencimiento"),
]