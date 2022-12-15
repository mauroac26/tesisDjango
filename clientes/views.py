from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, render, redirect
from .forms import clienteForm, editarCliForm
from .models import Clientes
from django.contrib import messages
# Create your views here.

@login_required
def index(request):

    cliente = Clientes.objects.all()

    data = {
        "clientes": cliente
    }
    return render(request, 'clientes/clientes.html', data)


@login_required
@permission_required('clientes.add_clientes', login_url='clientes')
def altaClientes(request):

    data = {
        "form": clienteForm()
    }
    
    if request.method == "POST":
        formulario = clienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, "El cliente se guardó correctamente")
            return redirect(to='clientes')
        else:
            data["form"] = formulario

    return render(request, 'clientes/altaCliente.html', data)


@login_required
@permission_required('clientes.change_clientes', login_url='clientes')
def editarCliente(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    
    data = {
        'form': editarCliForm(instance=cliente)
    }

    if request.method == "POST":
        formulario = editarCliForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, "El cliente se modificó correctamente")
            return redirect(to='clientes')
        data["form"] = editarCliForm()
            
    return render(request, 'clientes/editarCliente.html', data)


@login_required
@permission_required('clientes.delete_clientes', login_url='clientes')
def eliminarCliente(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    
    if cliente:
        cliente.delete()
        messages.add_message(request, messages.SUCCESS, "El cliente se eliminó correctamente")
        return redirect(to='clientes')
