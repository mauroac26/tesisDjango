from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .forms import editarProvForm, proveedorForm
from .models import proveedores

# Create your views here.
def index(request):

    proveedor = proveedores.objects.all()
    
    data = {
        "proveedores": proveedor
    }
    return render(request, 'proveedores/proveedores.html', data)


def altaProveedor(request):

    data = {
        'form': proveedorForm()
    }

    if request.method == "POST":
        formulario = proveedorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Proveedor guardado"
            return redirect(to='proveedores')
        else:
            data["form"] = formulario
    return render(request, 'proveedores/altaProveedor.html', data)



def editarProveedor(request, id):
    proveedor = get_object_or_404(proveedores, pk=id)
    
    data = {
        'form': editarProvForm(instance=proveedor)
    }

    if request.method == "POST":
        formulario = editarProvForm(data=request.POST, instance=proveedor)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Proveedor Modificado"
            return redirect(to='proveedores')
        data["form"] = editarProvForm()
            
    return render(request, 'proveedores/editarProveedor.html', data)


def eliminarProveedor(request, id):
    proveedor = get_object_or_404(proveedores, pk=id)
    
    if proveedor:
        proveedor.delete()
        return redirect(to='proveedores')



