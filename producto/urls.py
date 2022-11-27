from django.urls import path
from .views import editarCategoria, editarPromocion, eliminarCategoria, eliminarProducto, eliminarPromocion, index, marcas, categorias, altaCategorias, altaMarcas, altaProducto, editarProducto, editarMarca, eliminarMarca, prodPromocion, altaProductoPromo

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
    # path('vencimiento/', vencimiento, name="vencimiento"),
    # path('promocion/<id>', promocion, name="promocion"),
    path('altaProductoPromo/', altaProductoPromo, name="altaProductoPromo"),
    path('productosPromo/', prodPromocion.as_view(), name="productosPromo"),
    path('editarPromocion/<id>', editarPromocion, name="editarPromocion"),
    path('eliminarPromocion/<id>', eliminarPromocion, name="eliminarPromocion"),
]