from django import forms
from datetime import date
from .models import Compras, detalleCompra

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
            'fecha' : forms.DateInput(attrs={"type": "date", "value": date.today(), 'id': 'fecha'}),
            'cuit' : forms.TextInput(attrs={'id': 'cuit', 'readonly': True}),
            'iva' : forms.TextInput(attrs={'id': 'iva', 'readonly': True, 'class': 'text-center font-weight-bold text-white bg-info'}),
            'total' : forms.TextInput(attrs={'id': 'total', 'readonly': True, 'class': 'text-center font-weight-bold text-white bg-info'}),
            'subTotal' : forms.TextInput(attrs={'id': 'subTotal', 'readonly': True, 'class': 'text-center font-weight-bold text-white bg-info'}),
            'tipoComprobante': forms.Select(choices=tipo_Comprobante, attrs={'id': 'tipoComprobante'} )
        }


class detalleComprasForm(forms.ModelForm):

    class Meta:
        model = detalleCompra
        fields = '__all__'

