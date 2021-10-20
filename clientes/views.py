from django.shortcuts import get_object_or_404, render, redirect
from .forms import clienteForm, editarCliForm
from .models import Clientes
# Create your views here.

def index(request):

    cliente = Clientes.objects.all()

    data = {
        "clientes": cliente
    }
    return render(request, 'clientes/clientes.html', data)


def altaClientes(request):

    data = {
        "form": clienteForm()
    }
    
    if request.method == "POST":
        formulario = clienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Cliente guardado"
            return redirect(to='clientes')
        else:
            data["form"] = formulario

    return render(request, 'clientes/altaCliente.html', data)


def editarCliente(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    
    data = {
        'form': editarCliForm(instance=cliente)
    }

    if request.method == "POST":
        formulario = editarCliForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Proveedor Modificado"
            return redirect(to='clientes')
        data["form"] = editarCliForm()
            
    return render(request, 'clientes/editarCliente.html', data)


def eliminarCliente(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    
    if cliente:
        cliente.delete()
        return redirect(to='clientes')
