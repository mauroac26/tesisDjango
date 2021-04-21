from django import forms
from .models import Marca, Categoria, Producto

class marcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = '__all__'

class categoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'

class productoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'


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