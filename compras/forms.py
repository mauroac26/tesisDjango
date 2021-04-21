from django import forms
from datetime import date
from .models import Compras

tipo_Comprobante = [
    [0, "Factura"],
    [1, "Recibo"],
    [2, "Nota Credito"]
]

class comprasForm(forms.ModelForm):

    class Meta:
        model = Compras
        fields = ['comprobante', 'fecha', 'cuit', 'iva', 'total', 'subTotal', 'tipoComprobante']

        widgets = {
            'comprobante': forms.TextInput(attrs={'id': 'comprobante'}),
            'fecha' : forms.DateInput(attrs={"type": "date", "value": date.today()}),
            'cuit' : forms.TextInput(attrs={'id': 'cuit'}),
            'iva' : forms.TextInput(attrs={'id': 'iva'}),
            'total' : forms.TextInput(attrs={'id': 'total'}),
            'subTotal' : forms.TextInput(attrs={'id': 'subTotal'}),
            'tipoComprobante': forms.Select(choices=tipo_Comprobante)
        }
    

