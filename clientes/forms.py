from django import forms
from .models import Clientes

class clienteForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        super(clienteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'


class editarCliForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = '__all__'
        widgets = {
            'cuit': forms.TextInput(attrs={'id': 'cuit', 'readonly': True})
        }

    def __init__(self, *args, **kwargs):
        super(editarCliForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'