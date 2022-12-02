from django import forms

from ventas.models import tarjetaCredito
# from django.forms import Form
from .models import backup
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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




class reporteForm(forms.Form):
    
    fecha_rango = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'autocomplete': 'off' }))
    

class formBackup(forms.ModelForm):
    
    class Meta:
        model = backup
        fields = '__all__'