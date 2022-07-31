from django import forms
from .models import movCaja,  Caja

class movCajaForm(forms.ModelForm):

    class Meta:
        model = movCaja
        fields = ["descripcion", "operacion", "monto", "id_caja"]
        widgets = {
            'id_caja': forms.Select(attrs={'class': 'form-control form-control-sm'})
        }
        labels = {
            "id_caja": "Elegir caja:"
        }



class cajaForm(forms.ModelForm):

    class Meta:
        model = Caja
        fields = '__all__'


