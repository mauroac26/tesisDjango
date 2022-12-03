from datetime import date
from django import forms
from producto.models import Producto
from user.models import Users
from .models import Produccion


class produccionForm(forms.ModelForm):

    

    class Meta:
        model = Produccion
        exclude = ('estado', 'usuario')

        # usuarios = usuario()
            
    
        widgets = {
            'fecha' : forms.DateInput(attrs={"type": "date", "value": date.today(), 'id': 'fecha'}),
          
        }

    def __init__(self, *args, **kwargs):
        super(produccionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'

    # def __init__(self, *args, **kwargs):
        
    #     super(produccionForm, self).__init__(*args, **kwargs)
    #     self.fields['producto_retiro'] = forms.ModelChoiceField(queryset=Producto.objects.all(), initial=Producto.objects.get(id = 1))
        #self.fields['usuario'] =  forms.ModelChoiceField(queryset=Users.objects.all(), initial=Users.objects.get(id = self.user.id))
        #self.fields['usuario'].widget.attrs['disabled'] = 'disabled'

# class pediodosForm(forms.ModelForm):

#     class Meta:
#         model = Pedido
#         fields = '__all__'

#         # usuarios = usuario()
            
    
#         widgets = {
#             'fecha' : forms.DateInput(attrs={"type": "date", "value": date.today(), 'id': 'fecha'}),
          
#         }
