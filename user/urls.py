from django.urls import path

from user.views import configuracion, registro


urlpatterns = [
    path('registro/', registro, name="registro"),
    path('configuracion/', configuracion, name="configuracion"),

]