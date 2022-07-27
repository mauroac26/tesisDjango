from django import forms
from .models import movCaja,  Caja

class movCajaForm(forms.ModelForm):

    class Meta:
        model = movCaja
        fields = ["descripcion", "operacion", "monto"]



class cajaForm(forms.ModelForm):

    class Meta:
        model = Caja
        fields = '__all__'


    