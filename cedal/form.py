from django import forms
from .models import formaPago
from .validators import minValueValidator
from compras.models import detalleCompra

class formPago(forms.ModelForm):
    
    efectivo = forms.DecimalField(min_value=0, initial=0.00)
    credito = forms.DecimalField(min_value=0, initial=0.00)
    debito = forms.DecimalField(min_value=0, initial=0.00)
    cuotas = forms.IntegerField(min_value=0, initial=0)

    # def clean_efectivo(self):
    #     efectivo = self.cleaned_data["efectivo"]
    class Meta:
        model = formaPago
        fields = '__all__'

        widgets = {
            # 'efectivo': forms.TextInput(attrs={'id': 'efectivo', 'readonly': True, 'value':0.00}),
            # 'credito' : forms.TextInput(attrs={'id': 'credito', 'readonly': True, 'value':0.00}),
            # 'debito' : forms.TextInput(attrs={'id': 'debito', 'readonly': True, 'value':0.00}),
            # 'cuotas' : forms.TextInput(attrs={'id': 'cuotas', 'readonly': True, 'value':0}),
            'tipoCredito' : forms.Select(attrs={'id': 'tipoCredito'}),
            'tipoDebito': forms.Select(attrs={'id': 'tipoDebito'})
        }

        # efectivo = forms.DecimalField(min_value=0, initial=0)
        # credito = forms.DecimalField(min_value=0)
        # debito = forms.DecimalField(min_value=0)