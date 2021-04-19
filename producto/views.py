from django.shortcuts import render, redirect
from .forms import marcaForm, categoriaForm, productoForm
from .models import Marca, Categoria, Producto
from django.http import JsonResponse
# Create your views here.
def index(request):
    
    producto = Producto.objects.all()

    data = {
        "productos": producto
    }
    return render(request, 'producto/producto.html', data)


def altaProducto(request):

    data = {
        "form": productoForm()
    }

    if request.method == "POST":
        formulario = productoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto guardado"
            return redirect(to='productos')
        else:
            data["form"] = formulario

    return render(request, 'producto/altaProducto.html', data)


def marcas(request):
    
    marca = Marca.objects.all()

    data = {
        "marcas" : marca
    }
    return render(request, 'producto/marcas.html', data)


def categorias(request):
    
    categoria = Categoria.objects.all()

    data = {
        "categorias": categoria
    }
    return render(request, 'producto/categorias.html', data)


def altaCategorias(request):
    
    data = {
        'form': categoriaForm()
    }

    if request.method == "POST":
        formulario = categoriaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Categoria guardada"
        else:
            data["form"] = formulario

    return render(request, 'producto/altaCategorias.html', data)


def altaMarcas(request):
    
    data = {
        'form': marcaForm()
    }

    if request.method == "POST":
        formulario = marcaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Marca guardada"
        else:
            data["form"] = formulario

    return render(request, 'producto/altaMarcas.html', data)



