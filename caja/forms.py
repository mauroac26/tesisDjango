from django import forms
from .models import movCaja

class cajaForm(forms.ModelForm):

    class Meta:
        model = movCaja
        fields = ["descripcion", "operacion", "monto"]