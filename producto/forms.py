from unicodedata import category
from django import forms
from .models import Marca, Categoria, Producto

class marcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(marcaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'

class categoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(categoriaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'


class productoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        super(productoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'


class compraProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'codigo', 'precio_compra', 'stock']

        widgets = {
            'precio_compra': forms.TextInput(attrs={'id': 'precio', 'name': 'precio'}),
            'nombre': forms.TextInput(attrs={'id': 'nombreProducto', 'name': 'nombreProducto'}),
            'codigo': forms.TextInput(attrs={'id': 'codigo', 'name': 'codigo'}),
            'stock': forms.TextInput(attrs={'id': 'stock', 'name': 'stock'}),
        }


class  ventaProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'codigo', 'precio_venta', 'stock']

        widgets = {
            'precio_venta': forms.TextInput(attrs={'id': 'precio', 'name': 'precio'}),
            'nombre': forms.TextInput(attrs={'id': 'nombreProducto', 'name': 'nombreProducto'}),
            'codigo': forms.TextInput(attrs={'id': 'codigo', 'name': 'codigo'}),
            'stock': forms.TextInput(attrs={'id': 'stock', 'name': 'stock'}),
        }