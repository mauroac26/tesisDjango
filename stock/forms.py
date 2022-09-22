from django import forms

from stock.models import ajusteStock, detalleAjuste, stock

class ajusteForm(forms.ModelForm):
    
    class Meta:
        model = ajusteStock
        fields = '__all__'


class detalleAjusteForm(forms.ModelForm):

    class Meta:
        model = detalleAjuste
        fields = ['id_ajuste', 'id_producto', 'cantidad', 'motivo', 'detalle']

        widgets = {
            'cantidad': forms.TextInput(attrs={'id': 'cantidad', 'class': 'form-control form-control-sm'}),
            'motivo' : forms.Select(attrs={'id': 'motivo',  'class': 'form-control form-control-sm' }),
            'detalle': forms.Textarea(attrs={'id': 'detalle', 'class': 'form-control form-control-sm', 'rows': 3 })
        }



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