from django import forms
from .models import Caja

class cajaForm(forms.ModelForm):

    class Meta:
        model = Caja
        fields = ["descripcion", "operacion", "monto"]