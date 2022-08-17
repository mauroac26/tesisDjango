
from django.shortcuts import get_object_or_404, render, redirect

from compras.utils import render_pdf
from .forms import comprasForm, detalleComprasForm, formPagoCompra
from producto.forms import compraProductoForm
from .models import Compras, detalleCompra, formaPagoCompra
from producto.models import Producto
from django.http import JsonResponse
from proveedores.models import proveedores
from django.http import HttpResponse
from caja.forms import movCajaForm, movimientoCajaForm
from caja.models import Caja, movCaja
from datetime import datetime
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@login_required
@permission_required('compras.view_compras', login_url='index')
def index(request):


    compra = detalleCompra.objects.values('id_compra__id', 'id_compra__comprobante', 'id_compra__cuit__nombre', 'id_compra__fecha').annotate(Sum('total'))


    data = {
        "compras": compra
    }


    return render(request, 'compras/compras.html', data)

@login_required
@permission_required('compras.add_compras', login_url='compras')
def altaCompra(request):

    data = {
        "form": compraProductoForm()
    }

    data["formCompra"] = comprasForm()

    data["formPago"] = formPagoCompra()

    

    return render(request, 'compras/altaCompra.html', data)


def productoAutocomplete(request):
   
    if 'term' in request.GET:

        producto = Producto.objects.filter(nombre__icontains=request.GET.get("term"))
        nombre = list()
        if producto:
            
            for n in producto:
                if n.stock > n.stock_min:
                    color = "badge-success"
                elif n.stock <= n.stock_min:
                    color = "badge-warning"
                else:
                    color = "badge-danger"
                
                signer_json = {}
                signer_json['id'] = n.id
                signer_json['label'] = '<li style="font-size: 13px;" class="list-group-item d-flex justify-content-between align-items-center"><div class="col-sm-4">'+str(n.nombre)+'</div><span class="badge '+str(color)+' badge-pill text-white">'+str(n.stock)+'</span><span class="float-right">$'+str(n.precio_venta)+'</span></li>'
                signer_json['value'] = n.nombre
                signer_json['stock'] = n.stock
                signer_json['codigo'] = n.codigo
                signer_json['precio'] = n.precio_compra
                nombre.append(signer_json)
            return JsonResponse(nombre, safe=False)
        else:
            signer_json = {}
            signer_json['n'] = 1
            signer_json['label'] = '<li class="list-group-item align-items-center"><div class="col-sm-4"><span class="badge badge-pill badge-danger">Dar alta producto</span></div></li>'
            nombre.append(signer_json)
            return JsonResponse(nombre, safe=False)

    


import json
def cargarCompra(request):

    data = {
        "form": compraProductoForm()
    }

    data["formCompra"] = comprasForm()
    
    if request.is_ajax():
        
        data={}
        
        data['cuit'] = request.POST.get('cuit')
        data['iva'] = request.POST('iva')
        data['total'] = request.POST.get('total')
        data['subTotal'] = request.POS.get('subTotal')
        data['comprobante'] = request.POST.get('comprobante')
        data['tipoComprobante'] = request.POST.cleaned_data['tipoComprobante']
        data['fecha'] = request.POST.get('fecha')
        
  
       
      

   
   

    return render(request, 'compras/altaCompra.html', data)
       
        



def proveedorAutocomplete(request):
   
    if 'term' in request.GET:

        proveedor = proveedores.objects.filter(nombre__icontains=request.GET.get("term"))
        nombre = list()
        if proveedor:
            for n in proveedor:
            
                
                signer_json = {}
            
                signer_json['label'] = n.nombre
                signer_json['condicion'] = n.condicion
                signer_json['cuit'] = n.cuit
            
                
                nombre.append(signer_json)
            return JsonResponse(nombre, safe=False)
        else:
            signer_json = {}
            signer_json['n'] = 1
            signer_json['label'] = '<li class="list-group-item align-items-center"><div class="col-sm-4"><span class="badge badge-pill badge-danger">Dar alta proveedor</span></div></li>'
            nombre.append(signer_json)
            return JsonResponse(nombre, safe=False)




   
def prueba(request):
   
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        
        # get the form data
        form = comprasForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            form.save()
            #ultima_compra = Compras.objects.order_by('id', 'fecha').last()
            return HttpResponse(True)
            

    # some error occured
    return JsonResponse({"error": "ingresar comprobante valido"}, status=400)

@login_required
def cargarDetalleCompra(request):

    if request.is_ajax():
        data = {}

        ultima_compra = Compras.objects.order_by('id', 'fecha').last()
        id_producto = request.GET['id_producto']
        cantidad = request.GET['cantidad']
        precio = Producto.objects.get(id=id_producto)
        
        
        total = int(cantidad) * float(precio.precio_compra)
        
        neto = float(total) / 1.21
        iva = float(neto) * 0.21
        

        data['id_compra'] = ultima_compra
        data['id_producto'] = id_producto
        data['cantidad'] = cantidad
        data['iva'] = "{0:.2f}".format(iva)
        data['subTotal'] = "{0:.2f}".format(neto)
        data['total'] = total
        
        
        formulario = detalleComprasForm(data)
        if formulario.is_valid():
            
            formulario.save()

            if id_producto:
                producto = Producto.objects.get(id=id_producto)
                stock = int(producto.stock) + int(cantidad)
                producto.stock = stock
                producto.save()
            messages.add_message(request, messages.SUCCESS, "La compra se confirmó exitosamente")

            return HttpResponse(True)
            
        

    return JsonResponse({"error": "Error"}, status=400)



@login_required
@permission_required('compras.view_detallecompra', login_url='compras')
def detallesCompra(request, id):
    
    compras = Compras.objects.filter(id=id).select_related('cuit')
    
    data = {
        "datos": compras
    }
    


    detalle = detalleCompra.objects.filter(id_compra=id).select_related('id_producto')
    
    iva = detalleCompra.objects.filter(id_compra=id).aggregate(Sum('iva'))
    subTotal = detalleCompra.objects.filter(id_compra=id).aggregate(Sum('subTotal'))
    total = detalleCompra.objects.filter(id_compra=id).aggregate(Sum('total'))
    

    data["iva"] = iva
    data["subTotal"] = subTotal
    data["total"] = total
    data["id"] = id
    data["detalles"] = detalle

        

    return render(request, 'compras/detalleCompra.html', data)




@login_required
def imprimir(request):
    return render(request, 'compras/imprimir.html')


def reporteCompras(request):

    
    compra = detalleCompra.objects.values('id_compra__id', 'id_compra__comprobante', 'id_compra__cuit__nombre', 'id_compra__fecha').annotate(Sum('total'))


    data = {
        "compras": compra,
        "fecha" : datetime.now()
    }

    pdf = render_pdf('compras/pdfCompras.html', data)

    return HttpResponse(pdf, content_type='application/pdf')

# from django.conf import settings
# import uuid

# def reporteExcel(request):
#     compra = detalleCompra.objects.values('id_compra__id', 'id_compra__comprobante', 'id_compra__cuit__nombre', 'id_compra__fecha').annotate(Sum('total'))
#     df = pd.DataFrame(compra)
#     df.to_excel("cedal/static/excel/sdf.xlsx", encoding="UTF-8", index=False)
#     #return HttpResponse(df)

# import xlwt

# def reporteComprasExcel(request):
#     hoy = datetime.now()
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename='f'compras{hoy}.xls'''

#     wb = xlwt.Workbook(encoding='utf-8')
#     ws = wb.add_sheet('Compras')

#     # Sheet header, first row
#     row_num = 0

#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True

#     columns = ['Comprobante', 'nombre', 'fecha', 'Total', ]

#     for col_num in range(len(columns)):
#         ws.write(row_num, col_num, columns[col_num], font_style)

#     # Sheet body, remaining rows
#     font_style = xlwt.XFStyle()

#     rows = detalleCompra.objects.values('id_compra__id', 'id_compra__comprobante', 'id_compra__cuit__nombre', 'id_compra__fecha').annotate(Sum('total')).values_list("id_compra__comprobante", "id_compra__cuit__nombre", "id_compra__fecha", "total")
#     for row in rows:
#         row_num += 1
#         for col_num in range(len(row)):
#             ws.write(row_num, col_num, row[col_num], font_style)

#     wb.save(response)
#     return response


def pago(request):
    compra = detalleCompra.objects.values('id_compra__id', 'id_compra__comprobante', 'id_compra__cuit__nombre', 'id_compra__fecha', 'id_compra__estado').annotate(Sum('total'))

    compratotal = list()

    data = {
        "compras": compra
    }

    for d in data["compras"]:
        pago = formaPagoCompra.objects.filter(id_compra=d['id_compra__id']).annotate(Sum('total'))
        saldo = 0
        for p in pago:
            saldo = float(p.total__sum) + saldo
            
        total = float(d['total__sum']) - saldo
        signer_json = {}
        signer_json['id'] = d['id_compra__id']
        signer_json['comprobante'] = d['id_compra__comprobante']
        signer_json['fecha'] = d['id_compra__fecha']
        signer_json['nombre'] = d['id_compra__cuit__nombre']
        signer_json['total'] = d['total__sum']
        signer_json['saldo'] = total
        signer_json['estado'] = d['id_compra__estado']
        
        compratotal.append(signer_json)

    data = {
        "compras": compratotal
    }


    
    
    

    return render(request, 'compras/pagos.html', data)


def registroPago(request):
    data= {
        "formPago": formPagoCompra()
        }

    if request.method == "POST":

        total = float(request.POST.get('total'))
        id_compra = request.POST.get('id_compra')
        tipoPago = request.POST.get('tipoPago')
        saldo = detalleCompra.objects.annotate(Sum('total')).values('total__sum', 'id_compra__comprobante').filter(id_compra=id_compra)
        for c in saldo:
            comprobante = c['id_compra__comprobante']
            deuda = c['total__sum']

        
        
        if total <= float(deuda):
            
                
            id = Caja.objects.order_by('id', 'total', 'estado').last()
            
            if tipoPago == '1':
                if id.estado:
                    if id.total >= total:
                        cargarPago(id_compra, total, tipoPago, deuda)
                        #Registra el monto pagado en movimientos de la caja si es en efectivo y la caja se encuentra abierta
                        fecha = datetime.now()
                        caja = {}
                        caja['descripcion'] = "Compra comprobante N° " + comprobante
                        caja['operacion'] = 1
                        caja['monto'] = total
                        caja['id_caja'] = id.id
                        caja['saldo'] = deuda
                        caja['fecha'] = fecha
                        formulario = movimientoCajaForm(caja)
                            
                        if formulario.is_valid():
                            post = formulario.save(commit=False)
                        
                            ultimo_saldo = movCaja.objects.latest('fecha').saldo
                                
                            post.saldo = float(ultimo_saldo) - float(total)
            
                            post.save()
                            messages.add_message(request, messages.SUCCESS, "La forma de pago se realizo exitosamente")
                            return redirect(to='pago')
                        else:
                            data["formPago"] = formulario
                    else:
                        messages.add_message(request, messages.ERROR, "El total a pagar en efectivo es menor al saldo de la caja")
                    return redirect(to='registroPago')
                else:
                    messages.add_message(request, messages.ERROR, "No se puede realizar el pago, la caja se encuentra cerrada")
                    return redirect(to='registroPago')
            else:
                cargarPago(id_compra, total, tipoPago, deuda)
                return redirect(to='pago')
                
        else:
            messages.add_message(request, messages.ERROR, "El monto seleccionado es diferente al monto total de la compra")
            data["formPago"] = formPagoCompra() 
    return render(request, 'compras/registroPago.html', data)


def cargarPago(id_compra, total, tipoPago, deuda):
    #Registra el pago en formaPagoCompra 
    data = {}
    data['id_compra'] = id_compra
    data['total'] = total
    data['tipoPago'] = tipoPago
    pago = formPagoCompra(data)
            
    if pago.is_valid(): 
        pago.save()
        #una vez registrado el pago compara si quedan deudas entre el monto pagado y el saldo total de la compra
        compra = Compras.objects.get(id=id_compra)
        pago = formaPagoCompra.objects.filter(id_compra=id_compra).annotate(Sum('total'))
        tot = 0.0
        for p in pago:
            tot = float(p.total__sum) + float(tot)
                    
        #si es igual el total y la deuda el estado de la compra pasa a pagado sino sigue estando en adeudado
        if float(tot) == float(deuda):
            compra.estado = 'Pagado'
            compra.save()
    


def compraAdeudada(request):
    if 'term' in request.GET:
        
        compras = detalleCompra.objects.annotate(Sum('total')).values('total__sum', 'id_compra__cuit__nombre', 'id_compra__fecha','id_compra').filter(id_compra__cuit__nombre__icontains=request.GET.get("term"), id_compra__estado = 'Adeudado')
        
        nombre = list()
        if compras:
            for n in compras:
                pago = formaPagoCompra.objects.filter(id_compra=n['id_compra']).annotate(Sum('total'))
                saldo = 0.0
                for p in pago:
                    saldo = float(p.total__sum) + float(saldo)
            
                total = float(n['total__sum']) - float(saldo)
                
                # fecha = n['id_compra__fecha']
                # fecha1 = datetime.datetime.strptime(fecha, '%Y-%m-%dT%H:%MZ').strftime("%d-%m-%Y")
                dicCompras = {}
                dicCompras['id'] = n['id_compra']
                dicCompras['label'] = '<li style="font-size: 11px;" class="list-group-item d-flex justify-content-between align-items-center"><div class="col-sm-5">'+str(n['id_compra__cuit__nombre'])+'</div><span>'+str(n['id_compra__fecha'])+'</span><span>$'+str(n['total__sum'])+'</span></li>'
                dicCompras['value'] = f'{n["id_compra__cuit__nombre"]} / {n["id_compra__fecha"]} / {n["total__sum"]}'
                dicCompras['total'] = float(total)
                
                nombre.append(dicCompras)
            return JsonResponse(nombre, safe=False)
        else:
            dicCompras = {}
            dicCompras['n'] = 1
            dicCompras['label'] = '<li style="font-size: 11px;" class="list-group-item align-items-center"><div class="col-sm-7"><span>No se encuentas compras adeudadas</span></div></li>'
            nombre.append(dicCompras)
            return JsonResponse(nombre, safe=False)


def detallePago(request):
    # pago = formaPago.objects.filter(id_compra=id).values('id_compra__comprobante', 'total', 'cuotas', 'tipoCredito')

    #data['pago'] = pago
    return render(request, 'compras/detallePago.html')


def reporteCompra(request):
    return render(request, 'compras/reporteCompras.html')


def eliminarCompra(request, id):
    compra = get_object_or_404(Compras, pk=id)
    
    if compra:
        compra.delete()
        return redirect(to='compras')
    

def eliminarPago(request, id):
    pago = formaPagoCompra.objects.filter(id_compra=id)
    
    if pago:
        pago.delete()
        return redirect(to='pago')
    
    


