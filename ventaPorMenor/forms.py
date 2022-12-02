from datetime import date
from django import forms
from .models import DetalleventaPorMenor, ventaPorMenor


class ventaPorMenorForm(forms.ModelForm):

    class Meta:
        model = ventaPorMenor
        fields = '__all__'

      


class detalleVentaPorMenorForm(forms.ModelForm):

    class Meta:
        model = DetalleventaPorMenor
        fields = ['id_ventaPorMenor', 'producto', 'cantidad']

        widgets = {
            'id_ventaPorMenor': forms.HiddenInput(attrs={'required': False}),
            'producto': forms.Select(attrs={'id': 'producto'}),
            'cantidad' : forms.TextInput(attrs={'id': 'cantidad'}),
        }


    def __init__(self, *args, **kwargs):
            super(detalleVentaPorMenorForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control form-control-sm'