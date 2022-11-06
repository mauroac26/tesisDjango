from datetime import date
from django import forms

from stock.models import ajusteStock, stock
from user.models import Users

class ajusteForm(forms.ModelForm):
    
    class Meta:
        model = ajusteStock
        fields = ['fecha', 'id_producto', 'cantidad', 'motivo', 'detalle']

        widgets = {
            'detalle': forms.Textarea(attrs={'id': 'detalle', 'class': 'form-control form-control-sm', 'rows': 3 }),
            'fecha' : forms.DateInput(attrs={"type": "date", "value": date.today(), 'id': 'fecha'}),
            #'usuario': forms.TextInput(attrs={'id': 'usuario', 'class': 'form-control form-control-sm', "value": user.username,}),
        }

    # def __init__(self, *args, **kwargs):
        
    #     super(ajusteForm, self).__init__(*args, **kwargs)
    #     self.fields['usuario'] =  forms.ModelChoiceField(queryset=Users.objects.all(), initial=Users.objects.get(id = self.user.id))
    #     self.fields['usuario'].widget.attrs['disabled'] = 'disabled'
            

# class detalleAjusteForm(forms.ModelForm):

#     class Meta:
#         model = ajusteStock
#         fields = ['id_ajuste', 'id_producto', 'cantidad', 'motivo', 'detalle']

#         widgets = {
#             'cantidad': forms.TextInput(attrs={'id': 'cantidad', 'class': 'form-control form-control-sm'}),
#             'motivo' : forms.Select(attrs={'id': 'motivo',  'class': 'form-control form-control-sm' }),
#             'detalle': forms.Textarea(attrs={'id': 'detalle', 'class': 'form-control form-control-sm', 'rows': 3 })
#         }



class stockForm(forms.ModelForm):

    class Meta:
        model = stock
        fields = '__all__'

# class ajusteForm(forms.ModelForm):
    
#     class Meta:
#         model = ajusteStock
#         fields = ['stockNuevo', 'detalle']

#         widgets = {
#             'stockNuevo': forms.TextInput(attrs={'id': 'stockNuevo', 'required': True}),
#             'detalle': forms.Textarea(attrs={'id': 'detalle', 'required': True})
#         }
#         def __init__(self, *args, **kwargs):
#             super(ajusteForm, self).__init__(*args, **kwargs)
#             for visible in self.visible_fields():
#                 visible.field.widget.attrs['class'] = 'form-control form-control-sm'