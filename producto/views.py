from datetime import datetime, date
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .forms import marcaForm, categoriaForm, productoForm, promocionForm
from .models import Marca, Categoria, Producto

from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
@login_required
def index(request):
    
    producto = Producto.objects.all()

    data = {
        "productos": producto
    }
    return render(request, 'producto/producto.html', data)

@login_required
@permission_required('producto.add_producto', login_url='productos')
def altaProducto(request):

    data = {
        "form": productoForm()
    }

    if request.method == "POST":
        formulario = productoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, "El producto se guardó exitosamente")
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

@login_required
@permission_required('producto.add_categoria', login_url='categorias')
def altaCategorias(request):
    
    data = {
        'form': categoriaForm()
    }

    if request.method == "POST":
        formulario = categoriaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, "La categoria se guardó exitosamente")
            return redirect(to='categorias')
        else:
            data["form"] = formulario

    return render(request, 'producto/altaCategorias.html', data)

@login_required
@permission_required('producto.add_marca', login_url='marcas')
def altaMarcas(request):
    
    data = {
        'form': marcaForm()
    }

    if request.method == "POST":
        formulario = marcaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, "La marca se guardó exitosamente")
            return redirect(to='marcas')
        else:
            data["form"] = formulario

    return render(request, 'producto/altaMarcas.html', data)

@login_required
@permission_required('producto.change_producto', login_url='productos')
def editarProducto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    
    data = {
        'form': productoForm(instance=producto)
    }

    if request.method == "POST":
        formulario = productoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, "El producto se modificó exitosamente")
            return redirect(to='productos')
        data["form"] = productoForm()
            
    return render(request, 'producto/editarProducto.html', data)


@login_required
@permission_required('producto.delete_producto', login_url='productos')
def eliminarProducto(request, id):
    producto = get_object_or_404( Producto, pk=id)
    
    if producto:
        producto.delete()
        messages.add_message(request, messages.SUCCESS, "El producto se eliminó exitosamente")
        return redirect(to='productos')


@login_required
@permission_required('producto.change_marca', login_url='marcas')
def editarMarca(request, id):
    marca = get_object_or_404(Marca, pk=id)
    
    data = {
        'form': marcaForm(instance=marca)
    }

    if request.method == "POST":
        formulario = marcaForm(data=request.POST, instance=marca)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, "La marca se modificó exitosamente")
            return redirect(to='marcas')
        data["form"] = marcaForm()
            
    return render(request, 'producto/editarMarca.html', data)


@login_required
@permission_required('producto.delete_marca', login_url='marcas')
def eliminarMarca(request, id):
    print(id)
    marca = get_object_or_404(Marca, pk=id)
    
    if marca:
        marca.delete()
        messages.add_message(request, messages.SUCCESS, "La marca se eliminó exitosamente")
        return redirect(to='marcas')


@login_required
@permission_required('producto.change_categoria', login_url='categorias')
def editarCategoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    
    data = {
        'form': categoriaForm(instance=categoria)
    }

    if request.method == "POST":
        formulario = categoriaForm(data=request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, "La categoria se modificó exitosamente")
            return redirect(to='categorias')
        data["form"] = categoriaForm()
            
    return render(request, 'producto/editarCategoria.html', data)


@login_required
@permission_required('producto.delete_categoria', login_url='categorias')
def eliminarCategoria(request, id):
    categoria = get_object_or_404( Categoria, pk=id)
    
    if categoria:
        categoria.delete()
        messages.add_message(request, messages.SUCCESS, "La categoria se eliminó exitosamente")
        return redirect(to='categorias')



def vencimiento(request):
    
    hoy =  date(datetime.now().year, datetime.now().month, datetime.now().day)
    resultado = list()
    producto = Producto.objects.values('id', 'codigo', 'nombre', 'vencimiento')

    for v in producto:
        
        if v['vencimiento'] != None:
            vencimiento = v['vencimiento']
            
            fecha = date(vencimiento.year, vencimiento.month, vencimiento.day)
            
            resultados = hoy - fecha

            if resultados.days >= 355:
                prodVencidos = {}
                prodVencidos['id'] = v['id']
                prodVencidos['codigo'] = v['codigo']
                prodVencidos['nombre'] = v['nombre']
                prodVencidos['dias'] = resultados.days
            
                
            
            

                resultado.append(prodVencidos)

    
    data = {
        'producto': resultado
    }

    return render(request, 'producto/vencimiento.html', data)

            
        
def promocion(request, id):
    producto = get_object_or_404(Producto, pk=id)
    
    data = {
        'form': promocionForm(instance=producto),
        'nombre': producto.nombre
    }

    if request.method == "POST":
        formulario = promocionForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, "Se añadió el descuento correctamente")
            return redirect(to='productos')
        data["form"] = promocionForm()
            
    return render(request, 'producto/promocion.html', data)

    


