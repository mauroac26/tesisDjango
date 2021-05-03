from django.shortcuts import render, redirect
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

# Create your views here.
def index(request):

    compra = Compras.objects.all().select_related('cuit')
    data = {
        "compras": compra
    }
    return render(request, 'compras/compras.html', data)


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
        

    return render(request, 'compras/altaCompra.html', data)


def productoAutocomplete(request):
   
    if 'term' in request.GET:

        producto = Producto.objects.filter(nombre__icontains=request.GET.get("term"))
        nombre = list()
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
        data['tipoComprobante'] = request.POST.get('tipoComprobante')
        data['fecha'] = request.POST.get('fecha')
        
        
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
        for n in proveedor:
           
            
            signer_json = {}
           # signer_json['id'] = n.id
            signer_json['label'] = n.nombre
            signer_json['condicion'] = n.condicion
            signer_json['cuit'] = n.cuit
           
            
            nombre.append(signer_json)
        return JsonResponse(nombre, safe=False)
    
    return render(request, 'compras/altaCompra.html')



   
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
    return JsonResponse({"error": "ingresar compribante valido"}, status=400)


def cargarDetalleCompra(request):

    if request.is_ajax():
        data = {}

        ultima_compra = Compras.objects.order_by('id', 'fecha').last()
        id_producto = request.GET['id_producto']
        cantidad = request.GET['cantidad']
        total = request.GET['total']

        data['id_compra'] = ultima_compra
        data['id_producto'] = id_producto
        data['cantidad'] = cantidad
        data['total'] = total
        
        formulario = detalleComprasForm(data)
        if formulario.is_valid():
            
            formulario.save()
            return HttpResponse(True)
            
    return JsonResponse({"error": "Error"}, status=400)


def detallesCompra(request, id):
    
    compras = Compras.objects.filter(id=id).select_related('cuit')
    
    detalle = detalleCompra.objects.filter(id_compra=id).select_related('id_producto')

    data = {
        "datos": compras
    }
    
    data["detalles"] = detalle

    return render(request, 'compras/detalleCompra.html', data)



def cargarFormaPago(request):
    
    if request.is_ajax():
        data = {}

        ultima_compra = Compras.objects.order_by('id', 'fecha').last()
        efectivo = request.GET['efectivo']
        credito = request.GET['credito']
        debito = request.GET['debito']
        cuotas = request.GET['cuotas']
        tipoCredito = request.GET['tipoCredito']
        tipoDebito = request.GET['tipoDebito']
  
        data['id_compra'] = ultima_compra
        data['efectivo'] = efectivo
        data['credito'] = credito
        data['debito'] = debito
        data['cuotas'] = cuotas
        data['tipoCredito'] = tipoCredito
        data['tipoDebito'] = tipoDebito
        
        formulario = formPago(data)
        if formulario.is_valid():
            
            formulario.save()
        
        
        if efectivo > "":
            
            ultimo_saldo = Caja.objects.latest('fecha').saldo
            
            #fecha = Compras.objects.latest('fecha').fecha
           
            saldo = float(ultimo_saldo) - float(efectivo)
            
            caja = {} 
            
            caja['fecha'] = datetime.now()
            caja['descripcion'] = "Compra comprobante N°"
            caja['operacion'] = 1
            caja['monto'] = efectivo 
            caja['saldo'] = saldo

            formulario = cajaForm(caja)
            
            if formulario.is_valid():
            
                formulario.save()
            
    return JsonResponse({"error": "Error"}, status=400)