from datetime import date
from django import forms
from user.models import Users
from .models import Pedido, Produccion


class produccionForm(forms.ModelForm):

    

    class Meta:
        model = Produccion
        fields = '__all__'

        # usuarios = usuario()
            
    
        widgets = {
            'fecha' : forms.DateInput(attrs={"type": "date", "value": date.today(), 'id': 'fecha'}),
          
        }

    # def __init__(self, *args, **kwargs):
        
    #     super(produccionForm, self).__init__(*args, **kwargs)
    #     self.fields['usuario'] =  forms.ModelChoiceField(queryset=Users.objects.all(), initial=Users.objects.get(id = self.user.id))
    #     self.fields['usuario'].widget.attrs['disabled'] = 'disabled'

class pediodosForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = '__all__'

        # usuarios = usuario()
            
    
        widgets = {
            'fecha' : forms.DateInput(attrs={"type": "date", "value": date.today(), 'id': 'fecha'}),
          
        }
