from django.db import models

from base.models import BaseModel
from producto.models import Producto
from user.models import Users

# Create your models here.
class ventaPorMenor(BaseModel):
    fecha = models.DateField()
    usuario = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        
        verbose_name = 'ventaPorMenor'
        verbose_name_plural = 'ventaPorMenor'

    def __int__(self):
        return self.id


class DetalleventaPorMenor(BaseModel):
    id_ventaPorMenor = models.ForeignKey(ventaPorMenor, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Producto")
    cantidad = models.IntegerField(null=False, verbose_name="Cantidad", default=1)

    class Meta:
        
        verbose_name = 'DetalleventaPorMenor'
        verbose_name_plural = 'DetalleventaPorMenor'

    def __int__(self):
        return self.id