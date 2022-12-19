from datetime import date
from django import forms

from ventas.models import Ventas, detalleVenta, formaPagoVenta


tipo_Comprobante = [
    [0, "Factura"],
    [1, "Recibo"],
    [2, "Nota Credito"]
]

class ventasForm(forms.ModelForm):
    

    class Meta:
        model = Ventas
        fields = ['comprobante', 'fecha', 'cuit', 'tipoComprobante']

        widgets = {
            'comprobante': forms.TextInput(attrs={'id': 'comprobante', 'required': True}),
            'fecha' : forms.DateInput(attrs={"type": "date", "value": date.today(), 'id': 'fecha'}),
            'cuit' : forms.TextInput(attrs={'id': 'cuit', 'readonly': True}),
            'tipoComprobante': forms.Select(attrs={'id': 'tipoComprobante'} )
        }

    def clean_comprobante(self):
        comprobante = self.cleaned_data['comprobante']
        comprobante_taken = Ventas.objects.filter(comprobante=comprobante).exists()
        if comprobante_taken :
            raise forms.ValidationError('Comprobante existente')
        

    def __init__(self, *args, **kwargs):
        super(ventasForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'

class detalleVentaForm(forms.ModelForm):

    class Meta:
        model = detalleVenta
        fields = '__all__'


    def __init__(self, *args, **kwargs):
            super(detalleVentaForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control form-control-sm'

class formPagoVenta(forms.ModelForm):

    class Meta:
        model = formaPagoVenta
        fields = ['id_venta', 'total', 'cuotas', 'tipoPago', 'tipoCredito', 'fecha']

        widgets = {
            'id_venta': forms.TextInput(attrs={'id': 'id_venta'}),
            'total': forms.TextInput(attrs={'id': 'total','class': 'form-control form-control-sm' }),
            'tipoPago': forms.Select(attrs={'id': 'tipoPago','class': 'form-control form-control-sm'}),
            'tipoCredito': forms.Select(attrs={'id': 'tipoCredito','class': 'form-control form-control-sm'}),
            'cuotas': forms.TextInput(attrs={'id': 'cuotas','class': 'form-control form-control-sm'}),
        }
