from django import forms
from .models import formaPago

class formPago(forms.ModelForm):

    class Meta:
        model = formaPago
        fields = '__all__'

        widgets = {
            'efectivo': forms.TextInput(attrs={'id': 'efectivo'}),
            'credito' : forms.TextInput(attrs={'id': 'credito', 'readonly': True}),
            'debito' : forms.TextInput(attrs={'id': 'debito', 'readonly': True}),
            'cuotas' : forms.TextInput(attrs={'id': 'cuotas', 'readonly': True}),
            'tipoCredito' : forms.Select(attrs={'id': 'tipoCredito'}),
            'tipoDebito': forms.Select(attrs={'id': 'tipoDebito'})
        }