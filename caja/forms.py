from django import forms
from .models import movCaja,  Caja

class movCajaForm(forms.ModelForm):

    class Meta:
        model = movCaja
        fields = ["descripcion", "operacion", "monto"]
       
class movimientoCajaForm(forms.ModelForm):

    class Meta:
        model = movCaja
        fields = '__all__'


class cajaForm(forms.ModelForm):

    class Meta:
        model = Caja
        fields = '__all__'


class selectCaja(forms.ModelForm):

    class Meta:
        model = movCaja
        fields = ['id_caja']
        widgets = {
            'id_caja': forms.Select(attrs={'class': 'form-control form-control-sm'})
        }
        labels = {
            "id_caja": "Elegir caja:"
        }