from django import forms
import django
from django.forms import fields, widgets
from .models import formaPago, tarjetaCredito, tarjetaDebito
from .validators import minValueValidator
from compras.models import detalleCompra
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class formPago(forms.ModelForm):
    
    # efectivo = forms.DecimalField(min_value=0, initial=0.00)
    # credito = forms.DecimalField(min_value=0, initial=0.00)
    # debito = forms.DecimalField(min_value=0, initial=0.00)
    # cuotas = forms.IntegerField(min_value=0, initial=0)

    # def clean_efectivo(self):
    #     efectivo = self.cleaned_data["efectivo"]
    class Meta:
        model = formaPago
        fields = '__all__'

        widgets = {
            'id_compra': forms.TextInput(attrs={'id': 'id_compra'}),
            'total': forms.TextInput(attrs={'id': 'total','class': 'form-control form-control-sm' }),
            # 'credito' : forms.TextInput(attrs={'id': 'credito', 'readonly': True, 'value':0.00}),
            # 'debito' : forms.TextInput(attrs={'id': 'debito', 'readonly': True, 'value':0.00}),
            'cuotas' : forms.TextInput(attrs={'id': 'cuotas', 'class': 'form-control form-control-sm' }),
            'tipoCredito' : forms.Select(attrs={'id': 'tipoCredito', 'class': 'form-control form-control-sm' }),
            'tipoDebito': forms.Select(attrs={'id': 'tipoDebito', 'class': 'form-control form-control-sm' })
        }

        # efectivo = forms.DecimalField(min_value=0, initial=0)
        # credito = forms.DecimalField(min_value=0)
        # debito = forms.DecimalField(min_value=0)

nivel_usuario = [
    [0, "Administrador"],
    [1, "Vendedor"]
]

class UserRegisterForm(UserCreationForm):
    nivel = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=nivel_usuario)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'nivel', 'password1', 'password2']

class formCredito(forms.ModelForm):
    

    class Meta:
        model = tarjetaCredito
        fields = '__all__'


class formDebito(forms.ModelForm):
    

    class Meta:
        model = tarjetaDebito
        fields = '__all__'