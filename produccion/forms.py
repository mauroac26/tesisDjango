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

    # producto = 0
    # def clean_producto_retiro(self):
    #     id = self.cleaned_data['producto_retiro']
    #     producto = id.id
    #     return id

    def clean(self):
        cleaned_data = super().clean()
        cantidad = cleaned_data.get("cantidad_retiro")
        product = cleaned_data.get("producto_retiro")
        
        if cantidad > product.stock:
            raise forms.ValidationError("La cantidad seleccionada a retirar es mayor al stock del producto")
        else:
            return cleaned_data

    def __init__(self, *args, **kwargs):
        super(produccionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'

    # def clean_producto_retiro(self):
    #     id = self.cleaned_data['producto_retiro']
    #     print(id.id)
        # fecha = id.vencimiento_carnet
        
        # fechaVen = date(fecha.year, fecha.month, fecha.day)
        # hoy = date(datetime.now().year, datetime.now().month, datetime.now().day)
        
        # if hoy > fechaVen:
        #     raise forms.ValidationError("El carnet se encuentra vencido")
        # return id

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
