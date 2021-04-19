from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import proveedorForm
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

