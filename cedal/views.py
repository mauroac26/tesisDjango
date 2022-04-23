import json
from json.encoder import JSONEncoder
from django.contrib import messages
from django.shortcuts import redirect, render
from django.db.models import Sum
from cedal.models import tarjetaCredito, tarjetaDebito
from compras.models import detalleCompra
from django.http import HttpResponse, response
from django.http import JsonResponse
from django.db.models.functions import Extract
from .form import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

@login_required
def index(request):
    # if request.is_ajax() and request.method == "POST":
    #     compra = detalleCompra.objects.values('id_compra__id', 'id_compra__comprobante', 'id_compra__fecha').annotate(Sum('total'))
    #     return HttpResponse(True)
    return render(request, 'cedal/index.html')

def graficoCompras(request):
    
    if request.is_ajax() and request.method == "GET":
        
        #compra = detalleCompra.objects.values('id_compra__fecha').annotate(Sum('total')).order_by(Extract('id_compra__fecha', 'month') )
        compra = detalleCompra.objects.values('id_compra__fecha__month').order_by('id_compra__fecha__month').annotate(Sum('total')) 
        #compra = detalleCompra.objects.values(month=TruncMonth('id_compra__fecha__month').order_by('id_compra__fecha').annotate(Sum('total'))
        # data = {
        #     'datos': compra
        # }
        

        return JsonResponse({"data": list(compra)})
        
    return render(request, 'cedal/index.html')


# @permission_required('app.add_user')
# def registro(request):
#     data = {
#         'form': UserRegisterForm()
#     }

#     if request.method == 'POST':
#         formulario = UserRegisterForm(data=request.POST)
#         if formulario.is_valid():
#             formulario.save()
#             # user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
#             # login(request, user)
#             messages.add_message(request, messages.SUCCESS, "Usuario creado correctamente")
#             return redirect(to="index")
#         data["form"] = formulario
#     return render(request, 'registration/registro.html', data)

@login_required
def configuracion(request):
    return render(request, 'cedal/configuracion.html')


@login_required
def credito(request):
    
    credito = tarjetaCredito.objects.all()
    debito = tarjetaDebito.objects.all()

    data = {
        "credito": credito,
        "debito": debito
    }
    return render(request, 'cedal/credito.html', data)


def altaTarjeta(request):
    
    # data = {
    #     'form': formCredito()
    # }

    data = {}

    if request.method == "POST":
        nombre = request.POST.get('nombre')
        tarjetas = request.POST.get('selectTarjetas')
        
        data['nombre'] = nombre
        if tarjetas == "0":
           
            formulario = formCredito(data)
        else:
            
            formulario = formDebito(data)

        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, "La tarjeta de credito se guardó exitosamente")
            return redirect(to='credito')
        else:
            messages.add_message(request, messages.ERROR, "Error al guardar los datos")

    return render(request, 'cedal/altaTarjetas.html')
    