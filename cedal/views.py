import datetime
import json
from json.encoder import JSONEncoder
from django.contrib import messages
from django.shortcuts import redirect, render
from django.db.models import Sum, Count
from cedal.models import tarjetaCredito, tarjetaDebito
from django.http import JsonResponse
from produccion.models import Pedido
from producto.models import Marca
from user.models import Users
from ventas.models import detalleVenta, Ventas
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
    resultado = list()
    if request.is_ajax() and request.method == "GET":
        

        #compra = detalleCompra.objects.filter(id_compra__fecha__year = "2022").values('id_compra__fecha__month').order_by('id_compra__fecha__month').annotate(Sum('total'))
        venta = detalleVenta.objects.all().values('id_venta__fecha__month').annotate(Sum('total')).order_by('id_venta__fecha__month')
        
        # for e in venta:
        #     fecha = e['id_venta__fecha']
            
        #     tablaProsiciones = {}
        #     tablaProsiciones['total'] = e['total__sum']
        #     tablaProsiciones['fecha'] = fecha

        #     resultado.append(tablaProsiciones)

        #     print(resultado)
        return JsonResponse({"data": list(venta)})
        
   


def graficoProductos(request):
    
    if request.is_ajax() and request.method == "GET":
        
        productos = detalleVenta.objects.all().select_related('id_producto').values('id_producto__nombre').annotate(Sum('cantidad'))      

        return JsonResponse({"producto": list(productos)})
        

    return render(request, 'cedal/index.html')


def graficoClientes(request):
    
    if request.is_ajax() and request.method == "GET":
        
        clientes = Ventas.objects.all().values('cuit__nombre').annotate(cantidad=Count('cuit')).order_by('-cantidad')

        return JsonResponse({"clientes": list(clientes)})

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
    

def cantidadPedidos(request):
    pedidos = 0
    if request.is_ajax() and request.method == "GET":
        pedidos = Pedido.objects.filter(estado='Pendiente').count()
        return JsonResponse({"data": pedidos})
        # usuario = request.user.id
        # grupo = Users.objects.filter(id=usuario).values('groups')
        # for p in grupo:
           
        #     if p['groups'] == 5:

        #         pedidos = Pedido.objects.filter(estado='Pendiente').count()
               
        # return JsonResponse({"data": pedidos})