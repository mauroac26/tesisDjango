from django import forms
from .models import movCaja,  Caja

class movCajaForm(forms.ModelForm):

    class Meta:
        model = movCaja
        fields = ["descripcion", "operacion", "monto"]

    
    def __init__(self, *args, **kwargs):
        super(movCajaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'
            
       
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