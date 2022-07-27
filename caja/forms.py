from django import forms
from .models import movCaja

class movCajaForm(forms.ModelForm):

    class Meta:
        model = movCaja
        fields = ["descripcion", "operacion", "monto"]