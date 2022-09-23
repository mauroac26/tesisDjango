from django import forms
from .models import proveedores

class proveedorForm(forms.ModelForm):

    class Meta:
        model = proveedores
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(proveedorForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'


class editarProvForm(forms.ModelForm):

    class Meta:
        model = proveedores
        fields = '__all__'
        widgets = {
            'cuit': forms.TextInput(attrs={'id': 'cuit', 'readonly': True})
        }


class proveedorCompraForm(forms.ModelForm):

    class Meta:
        model = proveedores
        fields = ['cuit']
        

        widgets = {
            'cuit': forms.TextInput(attrs={'readonly': True, 'id': 'cuit'})
        }
        