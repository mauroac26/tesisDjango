from django import forms
from .models import proveedores

class proveedorForm(forms.ModelForm):

    class Meta:
        model = proveedores
        fields = '__all__'



class proveedorCompraForm(forms.ModelForm):

    class Meta:
        model = proveedores
        fields = ['cuit']
        

        widgets = {
            'cuit': forms.TextInput(attrs={'disabled': True})
        }
        