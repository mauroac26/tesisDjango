from django.http.response import HttpResponseForbidden
from django.shortcuts import render, redirect

#import pandas as pd
from django.core import serializers
from compras.utils import render_pdf
from .forms import comprasForm, detalleComprasForm
from producto.forms import productoForm, compraProductoForm
from .models import Compras, detalleCompra
from proveedores.forms import proveedorCompraForm
from producto.models import Producto
from django.http import JsonResponse
from proveedores.models import proveedores
from django.http import HttpResponse
from django.core.cache import cache
from cedal.models import formaPago
from cedal.form import formPago
from caja.forms import cajaForm
from caja.models import Caja
from datetime import datetime
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
import pandas as pd
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

    data["formPago"] = formPago()

    
    # if request.method == "POST":
    #     formulario = comprasForm(data=request.POST)
    #     if formulario.is_valid(): 
    #         formulario.save()
            
    #         return redirect(to='compras')
            
    #     else:
    #         data["formCompra"] = formulario
        
    # def get(self, request, **kwargs):
    #     if not self.request.user.has_perm('compras.add_compras'):
    #         return HttpResponseForbidden()

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
                signer_json['label'] = '<li class="list-group-item d-flex justify-content-between align-items-center"><div class="col-sm-4">'+str(n.nombre)+'</div><span class="badge '+str(color)+' badge-pill text-white">'+str(n.stock)+'</span><span class="float-right">$'+str(n.precio_venta)+'</span></li>'
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

    
    #return render(request, 'compras/altaCompra.html')

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
        
        print(request.POST.cleaned_data['tipoComprobante'])
        # compra = comprasForm(data)

        # if compra.is_valid(): 
        #     compra.save()
        #     return HttpResponse('Success')
        '''
        detalle = {}
        
        detalle['cantidad'] = request.GET['cantidad']
        
        detalle['id_producto'] = request.GET['id_producto']
        cache.set(detalle)
        cache.set(detalle)
       '''
       
      

   
    # if request.method == "POST":
    #      print("chau")
        #print(cache.get_many(['cantidad', 'id_producto']))
         

    #     compra = comprasForm(data=request.POST)
        
    #     if compra.is_valid(): 
    #         compra.save()
            
    #         det = {}
    #         det= cache.get_many(['cantidad', 'id_producto'])
    #         print(det)
            # detalle = {}
            
            # detalle = cache.get_many(['cantidad', 'id_producto'])
            # print(detalle)
            # ultima_compra = Compras.objects.order_by('id', 'fecha').last()
            
           
            
            # for n in detalle:
            #     detalle['id_compra'] = ultima_compra
            
            # detalleCompra = detalleComprasForm(detalle)

            # if detalleCompra.is_valid():
            #    detalleCompra.save()
            # return redirect(to='compras')
            
        # else:
        #     data["formCompra"] = compra

    return render(request, 'compras/altaCompra.html', data)
       
        



def proveedorAutocomplete(request):
   
    if 'term' in request.GET:

        proveedor = proveedores.objects.filter(nombre__icontains=request.GET.get("term"))
        nombre = list()
        if proveedor:
            for n in proveedor:
            
                
                signer_json = {}
            # signer_json['id'] = n.id
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
    #return render(request, 'compras/altaCompra.html')



   
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

from decimal import Decimal

@login_required
@permission_required('compras.view_detallecompra', login_url='compras')
def detallesCompra(request, id):
    
    compras = Compras.objects.filter(id=id).select_related('cuit')
    
    data = {
        "datos": compras
    }
    
    data["pagos"] = formaPago.objects.filter(id_compra=id).select_related('tipoDebito').select_related('tipoCredito')

    data["formPago"] = formPago()

    detalle = detalleCompra.objects.filter(id_compra=id).select_related('id_producto')
    
    iva = detalleCompra.objects.filter(id_compra=id).aggregate(Sum('iva'))
    subTotal = detalleCompra.objects.filter(id_compra=id).aggregate(Sum('subTotal'))
    total = detalleCompra.objects.filter(id_compra=id).aggregate(Sum('total'))
    
    
    for d in data["datos"]:
        comprobante = d.comprobante
    data["iva"] = iva
    data["subTotal"] = subTotal
    data["total"] = total
    
    data["detalles"] = detalle

    if request.method == "POST":
        
        efectivo = float(request.POST.get('efectivo'))
        credito = float(request.POST.get('credito'))
        debito = float(request.POST.get('debito'))
        cuotas = request.POST.get('cuotas')
        tipoCredito = request.POST.get('tipoCredito')
        tipoDebito = request.POST.get('tipoDebito')

        sumaTotal = efectivo + credito + debito

        if sumaTotal == float(data['total']["total__sum"]):
            
            data['id_compra'] = id
            data['efectivo'] = efectivo
            data['credito'] = credito
            data['debito'] = debito
            data['cuotas'] = cuotas
            data['tipoCredito'] = tipoCredito
            data['tipoDebito'] = tipoDebito

            data['id_compra'] = id
            

            pago = formPago(data)
        
            if pago.is_valid(): 
                pago.save()
                
                messages.add_message(request, messages.SUCCESS, "La forma de pago se realizo exitosamente")
            
            if efectivo > 0:
                
                caja = {}
                caja['descripcion'] = "Compra comprobante N° " + comprobante
                caja['operacion'] = 1
                caja['monto'] = efectivo 

                formulario = cajaForm(caja)

                if formulario.is_valid():
                    post = formulario.save(commit=False)
            
                    ultimo_saldo = Caja.objects.latest('fecha').saldo
                    
                    post.saldo = float(ultimo_saldo) - float(efectivo)
            
                    fecha = datetime.now()
                    post.fecha = fecha
                    post.save()
            else:
                data["formPago"] = formPago() 
        else:
            messages.add_message(request, messages.ERROR, "El monto seleccionado es diferente al monto total de la compra")
            return render(request, 'compras/detalleCompra.html', data)
        

    return render(request, 'compras/detalleCompra.html', data)



# def cargarFormaPago(request):
    
#     if request.is_ajax():
#         data = {}

#         ultima_compra = Compras.objects.order_by('id', 'fecha').last()
#         efectivo = request.GET['efectivo']
#         credito = request.GET['credito']
#         debito = request.GET['debito']
#         cuotas = request.GET['cuotas']
#         tipoCredito = request.GET['tipoCredito']
#         tipoDebito = request.GET['tipoDebito']
  
#         data['id_compra'] = ultima_compra
#         data['efectivo'] = efectivo
#         data['credito'] = credito
#         data['debito'] = debito
#         data['cuotas'] = cuotas
#         data['tipoCredito'] = tipoCredito
#         data['tipoDebito'] = tipoDebito
        
#         formulario = formPago(data)
#         if formulario.is_valid():
            
#             formulario.save()
        
        
#         if efectivo > "":
            
#             ultimo_saldo = Caja.objects.latest('fecha').saldo
            
#             #fecha = Compras.objects.latest('fecha').fecha
           
#             saldo = float(ultimo_saldo) - float(efectivo)
            
#             caja = {} 
            
#             caja['fecha'] = datetime.now()
#             caja['descripcion'] = "Compra comprobante N°"
#             caja['operacion'] = 1
#             caja['monto'] = efectivo 
#             caja['saldo'] = saldo

#             formulario = cajaForm(caja)
            
#             if formulario.is_valid():
            
#                 formulario.save()
            
#     return JsonResponse({"error": "Error"}, status=400)


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

import xlwt

def reporteComprasExcel(request):
    hoy = datetime.now()
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename='f'compras{hoy}.xls'''

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Compras')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Comprobante', 'nombre', 'fecha', 'Total', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = detalleCompra.objects.values('id_compra__id', 'id_compra__comprobante', 'id_compra__cuit__nombre', 'id_compra__fecha').annotate(Sum('total')).values_list("id_compra__comprobante", "id_compra__cuit__nombre", "id_compra__fecha", "total")
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


    