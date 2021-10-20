from django import forms
from .models import Clientes

class clienteForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = '__all__'


class editarCliForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = '__all__'
        widgets = {
            'cuit': forms.TextInput(attrs={'id': 'cuit', 'readonly': True})
        }