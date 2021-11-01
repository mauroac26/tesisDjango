from django import forms
import django
from django.forms import fields, widgets
from .models import formaPago
from .validators import minValueValidator
from compras.models import detalleCompra
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
            #'efectivo': forms.TextInput(attrs={'class': 'form-control form-control-sm' }),
            # 'credito' : forms.TextInput(attrs={'id': 'credito', 'readonly': True, 'value':0.00}),
            # 'debito' : forms.TextInput(attrs={'id': 'debito', 'readonly': True, 'value':0.00}),
            # 'cuotas' : forms.TextInput(attrs={'id': 'cuotas', 'readonly': True, 'value':0}),
            'tipoCredito' : forms.Select(attrs={'id': 'tipoCredito'}),
            'tipoDebito': forms.Select(attrs={'id': 'tipoDebito'})
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

