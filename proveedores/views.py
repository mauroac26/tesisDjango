from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .forms import editarProvForm, proveedorForm
from .models import proveedores
from django.contrib import messages

# Create your views here.
@login_required
@permission_required('proveedores.view_proveedores', login_url='index')
def index(request):

    proveedor = proveedores.objects.all()
    
    data = {
        "proveedores": proveedor
    }
    return render(request, 'proveedores/proveedores.html', data)


@login_required
@permission_required('proveedores.add_proveedores', login_url='proveedores')
def altaProveedor(request):

    data = {
        'form': proveedorForm()
    }

    if request.method == "POST":
        formulario = proveedorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, "El proveedor se guardó correctamente")
            return redirect(to='proveedores')
        else:
            data["form"] = formulario
    return render(request, 'proveedores/altaProveedor.html', data)


@login_required
@permission_required('proveedores.change_proveedores', login_url='proveedores')
def editarProveedor(request, id):
    proveedor = get_object_or_404(proveedores, pk=id)
    
    data = {
        'form': editarProvForm(instance=proveedor)
    }

    if request.method == "POST":
        formulario = editarProvForm(data=request.POST, instance=proveedor)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, "El proveedor se modificó correctamente")
            return redirect(to='proveedores')
        data["form"] = editarProvForm()
            
    return render(request, 'proveedores/editarProveedor.html', data)


@login_required
@permission_required('proveedores.delete_proveedores', login_url='proveedores')
def eliminarProveedor(request, id):
    proveedor = get_object_or_404(proveedores, pk=id)
    
    if proveedor:
        proveedor.delete()
        messages.add_message(request, messages.SUCCESS, "El proveedor se eliminó correctamente")
        return redirect(to='proveedores')



