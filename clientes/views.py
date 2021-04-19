from django.shortcuts import render, redirect
from .forms import clienteForm
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