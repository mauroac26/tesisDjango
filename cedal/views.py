import datetime
from datetime import datetime, date
from django.contrib import messages
from django.shortcuts import redirect, render
from django.db.models.functions import Coalesce
from django.db.models import Sum, Count
from cedal.form import formBackup, formCredito, reporteForm
from cedal.models import backup
from django.http import JsonResponse
from compras.models import detalleCompra, formaPagoCompra
from produccion.models import Produccion
from producto.models import Marca, Producto, ProductoPromocion
from user.models import Users
from ventas.models import detalleVenta, Ventas, formaPagoVenta, tarjetaCredito

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
    

    data = {
        "credito": credito,
    }
    return render(request, 'cedal/credito.html', data)


def altaTarjeta(request):
    
    data = {
        'form': formCredito()
    }

    if request.method == "POST":
        
        
           
        formulario = formCredito(data=request.POST)
        

        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, "La tarjeta de credito se guardó exitosamente")
            return redirect(to='credito')
        else:
            data["form"] = formulario

    return render(request, 'cedal/altaTarjetas.html', data)
    

def cantidadPedidos(request):
    pedidos = 0
    if request.is_ajax() and request.method == "GET":
    
        pedidos = Produccion.objects.filter(estado='Pendiente').count()
        return JsonResponse({"data": pedidos})
        


# def prodVencimiento(request):
#     if request.is_ajax() and request.method == "GET":
#         hoy =  date(datetime.now().year, datetime.now().month, datetime.now().day)
#         resultado = list()
#         producto = Producto.objects.values('id', 'codigo', 'nombre', 'vencimiento')

#         for v in producto:
            
#             if v['vencimiento'] != None:
#                 vencimiento = v['vencimiento']
                
#                 fecha = date(vencimiento.year, vencimiento.month, vencimiento.day)
                
#                 resultados = hoy - fecha

#                 if resultados.days >= 355:
#                     prodVencidos = {}
#                     prodVencidos['id'] = v['id']
#                     prodVencidos['codigo'] = v['codigo']
#                     prodVencidos['nombre'] = v['nombre']
#                     prodVencidos['dias'] = resultados.days
                
                    
                
                

#                     resultado.append(prodVencidos)

#         return JsonResponse({"data": len(resultado)})


def consultaPromo():
    promo = ProductoPromocion.objects.all()
    hoy =  date(datetime.now().year, datetime.now().month, datetime.now().day)
    for p in promo:
        fecha = p.fechaFin
        fechaFin = date(fecha.year, fecha.month, fecha.day)
        if hoy > fechaFin:
            p.delete()


def reportesCompras(request):


    data = {
       
        "reporteForm": reporteForm()
    }


    return render(request, 'reportes/reporteCompras.html', data)


def comprasRango(request):
    if request.is_ajax():
       
        data = []
    
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']

    
        compras = detalleCompra.objects.values('id_compra__comprobante', 'id_compra__cuit__nombre', 'id_compra__cuit', 'id_compra__fecha',  'id_compra__formapagocompra__tipoPago').annotate(Sum('total'))
        
        if fecha_inicio and fecha_fin:
            
            compras = compras.filter(id_compra__fecha__range=[fecha_inicio, fecha_fin])
            
        for f in compras:
            if f['id_compra__formapagocompra__tipoPago'] == None:
                tipo = "Adeudado",
            else:
                tipo = f['id_compra__formapagocompra__tipoPago']

            data.append([
                f['id_compra__comprobante'],
                f['id_compra__cuit__nombre'],
                f['id_compra__cuit'],
                f['id_compra__fecha'],
                tipo,
                f['total__sum']
            ])

    else:
        data['error'] = 'Ha ocurrido un error'
    
    return JsonResponse(data, safe=False)



def reportesVentas(request):


    data = {
       
        "reporteForm": reporteForm()
    }


    return render(request, 'reportes/reporteVentas.html', data)


def ventasRango(request):
    if request.is_ajax():
       
        data = []
    
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']

    
        venta = detalleVenta.objects.values('id_venta__comprobante', 'id_venta__cuit__nombre', 'id_venta__cuit', 'id_venta__fecha').annotate(Sum('total')).annotate(Sum('iva')).annotate(Sum('subTotal'))
      
        

        if len(fecha_inicio) and len(fecha_fin):
            
            ventas = venta.filter(id_venta__fecha__range=[fecha_inicio, fecha_fin])
            
        for f in ventas:

            data.append([
                f['id_venta__comprobante'],
                f['id_venta__cuit__nombre'],
                f['id_venta__cuit'],
                f['id_venta__fecha'],
                f'${f["iva__sum"]}',
                f'${f["subTotal__sum"]}',
                f'${f["total__sum"]}'
            ])

    else:
        data['error'] = 'Ha ocurrido un error'
    
    return JsonResponse(data, safe=False)



def reportesCuentasPagar(request):


    data = {
       
        "reporteForm": reporteForm()
    }


    return render(request, 'reportes/reporteCuentasPagar.html', data)


def cuentasPagarRango(request):
    if request.is_ajax():
       
        data = []
    
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']

    
        compra = detalleCompra.objects.values('id_compra', 'id_compra__cuit__nombre', 'id_compra__fecha', 'id_compra__cuit', 'id_compra__estado').annotate(Sum('total')).filter(id_compra__estado="Adeudado")
        
        if len(fecha_inicio) and len(fecha_fin):
            
            compras = compra.filter(id_compra__fecha__range=[fecha_inicio, fecha_fin])
            for n in compras:
                
                pago = formaPagoCompra.objects.filter(id_compra=n['id_compra']).annotate(Sum('total'))
                saldo = 0.0
                for p in pago:
                    saldo = float(p.total__sum) + float(saldo)
            
                total = float(n['total__sum']) - float(saldo)

                data.append([
                    n['id_compra__cuit__nombre'],
                    n['id_compra__cuit'],
                    n['id_compra__fecha'],
                    f'${total}',
                    f'${n["total__sum"]}',
                    n['id_compra__estado']
                ])
        
            
       

            

    else:
        data['error'] = 'Ha ocurrido un error'
    
    return JsonResponse(data, safe=False)


def reportesCuentasCobrar(request):


    data = {
       
        "reporteForm": reporteForm()
    }


    return render(request, 'reportes/reporteCuentasCobrar.html', data)


def cuentasCobrarRango(request):
    if request.is_ajax():
       
        data = []
    
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']

    
        venta = detalleVenta.objects.values('id_venta', 'id_venta__cuit__nombre', 'id_venta__fecha', 'id_venta__cuit', 'id_venta__estado').annotate(Sum('total')).filter(id_venta__estado="Adeudado")
        
        if len(fecha_inicio) and len(fecha_fin):
            
            ventas = venta.filter(id_venta__fecha__range=[fecha_inicio, fecha_fin])
            for n in ventas:
                
                pago = formaPagoVenta.objects.filter(id_venta=n['id_venta']).annotate(Sum('total'))
                saldo = 0.0
                for p in pago:
                    saldo = float(p.total__sum) + float(saldo)
            
                total = float(n['total__sum']) - float(saldo)

                data.append([
                    n['id_venta__cuit__nombre'],
                    n['id_venta__cuit'],
                    n['id_venta__fecha'],
                    f'${total}',
                    f'${n["total__sum"]}',
                    n['id_venta__estado']
                ])
        
            
       

            

    else:
        data['error'] = 'Ha ocurrido un error'
    
    return JsonResponse(data, safe=False)



import subprocess, gzip
from subprocess import Popen
from proyectoTesis.settings import DATABASES, RUTA
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from zipfile import ZipFile




def backupBD(request):
    respaldo = backup.objects.all()

    data = {
        "respaldo": respaldo
    }

    if request.method == "POST":
        name = DATABASES['default']['NAME']
        passwd = DATABASES['default']['PASSWORD']
        user = DATABASES['default']['USER']
        ruta = RUTA

        fecha = datetime.now()
        fecha1 = fecha.strftime("%m-%d-%Y")
    
        proc = subprocess.Popen("mysqldump -u "+user+"  "+name+" > "f'{ruta}{fecha1}.sql', shell=True)
        proc.wait()

        fecha_respaldo = fecha
        usuario = request.user.id
         
        data = {}
        data['fecha'] = fecha_respaldo
        data['usuario'] = usuario
        data['archivo'] = f'{ruta}{fecha1}.sql'
        
        respaldo = formBackup(data)
                
        if respaldo.is_valid(): 
            respaldo.save()
            messages.add_message(request, messages.SUCCESS, "El backup de la base de datos se realizó correctamente")
            return redirect(to='backup')
        else:
            messages.add_message(request, messages.ERROR, "El backup de la base de datos no se pudo realizar")

    return render(request, 'configuracion/backup.html', data)

    
    
