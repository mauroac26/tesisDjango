from django import forms
from datetime import date
from .models import Compras, detalleCompra, formaPagoCompra


# tipo_Comprobante = [
#     [0, "Factura"],
#     [1, "Recibo"],
#     [2, "Nota Credito"]
# ]

class comprasForm(forms.ModelForm):
    
    

    class Meta:
        model = Compras
        fields = ['comprobante', 'fecha', 'cuit', 'tipoComprobante']

        widgets = {
            'comprobante': forms.TextInput(attrs={'id': 'comprobante', 'required': True}),
            'fecha' : forms.DateInput(attrs={"type": "date", "value": date.today(), 'id': 'fecha'}),
            'cuit' : forms.TextInput(attrs={'id': 'cuit', 'readonly': True}),
            'tipoComprobante': forms.Select(attrs={'id': 'tipoComprobante'} )

        }

    def clean_comprobante(self):
        comprobante = self.cleaned_data['comprobante']
        comprobante_taken = Compras.objects.filter(comprobante=comprobante).exists()
        if comprobante_taken :
            raise forms.ValidationError('Comprobante existente')
        return comprobante
        
    # def clean_comprobante(self):
    #     comprobante = self.cleaned_data["comprobante"]
        
    #     existe = Compras.objects.filter(comprobante__iexact=comprobante).exists()
        
    #     if existe:
            
    #         raise forms.ValidationError("El numero de comprobante ya existe")
        
    #     return comprobante

    def __init__(self, *args, **kwargs):
        super(comprasForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'    

    


class detalleComprasForm(forms.ModelForm):

    class Meta:
        model = detalleCompra
        fields = '__all__'


class formPagoCompra(forms.ModelForm):
    
    # efectivo = forms.DecimalField(min_value=0, initial=0.00)
    # credito = forms.DecimalField(min_value=0, initial=0.00)
    # debito = forms.DecimalField(min_value=0, initial=0.00)
    # cuotas = forms.IntegerField(min_value=0, initial=0)

    # def clean_efectivo(self):
    #     efectivo = self.cleaned_data["efectivo"]
    class Meta:
        model = formaPagoCompra
        fields = ['id_compra', 'total', 'tipoPago', 'fecha']

        widgets = {
            'id_compra': forms.TextInput(attrs={'id': 'id_compra'}),
            'total': forms.TextInput(attrs={'id': 'total','class': 'form-control form-control-sm' }),
            'tipoPago': forms.Select(attrs={'id': 'tipoPago','class': 'form-control form-control-sm'})
        }
