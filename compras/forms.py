from django import forms
from datetime import date
from .models import Compras

tipo_Comprbante = [
    [0, "Factura"],
    [1, "Recibo"],
    [2, "Nota Credito"]
]

class comprasForm(forms.ModelForm):

    class Meta:
        model = Compras
        fields = '__all__'

        widgets = {
            'comprobante': forms.TextInput(attrs={'id': 'comprobante'}),
            'fecha' : forms.DateInput(attrs={"type": "date"}),
            #'tipoComprobante': forms.Select(choices=tipo_Comprbante)
        }
    

