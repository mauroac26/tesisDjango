from django.urls import path

from user.views import cambiarPassword, editarUsuario, eliminarUsuario, registro, usuarios, editarPerfilUsuario


urlpatterns = [
    path('registro/', registro, name="registro"),
    #path('configuracion/', configuracion, name="configuracion"),
    path('usuarios/', usuarios, name="usuarios"),
    path('editarUsuario/<id>', editarUsuario, name="editarUsuario"),
    path('eliminarUsuario/<id>', eliminarUsuario, name="eliminarUsuario"),
    path('editarPerfilUsuario/', editarPerfilUsuario, name="editarPerfilUsuario"),
    path('cambiarPassword/', cambiarPassword, name="cambiarPassword"),
]
