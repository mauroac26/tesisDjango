from django.shortcuts import get_object_or_404, render, redirect
from .forms import comprasForm, detalleComprasForm, formPagoCompra
from producto.forms import compraProductoForm
from .models import Compras, detalleCompra, formaPagoCompra
from producto.models import Producto
from django.http import JsonResponse
from proveedores.models import proveedores
from django.http import HttpResponse
from caja.forms import movimientoCajaForm
from caja.models import Caja, movCaja
from datetime import datetime
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from stock.views import cargarStock, eliminarStock

# Create your views here.
#Muesta las compras realizadas
@login_required
@permission_required('compras.view_compras', login_url='index')
def index(request):

 
    compra = detalleCompra.objects.values('id_compra__id', 'id_compra__comprobante', 'id_compra__cuit__nombre', 'id_compra__fecha').annotate(Sum('total'))


    data = {
        "compras": compra
    }


    return render(request, 'compras/compras.html', data)


#Mustra la interfaz y los formularios para dar de alta una compra
@login_required
@permission_required('compras.add_compras', login_url='compras')
def altaCompra(request):

    data = {
        "form": compraProductoForm()
    }

    data["formCompra"] = comprasForm()

    data["formPago"] = formPagoCompra()

    

    return render(request, 'compras/altaCompra.html', data)


#Obtiene lista de productos

def productoAutocomplete(request):
   
    if 'term' in request.GET:

        producto = Producto.objects.filter(nombre__icontains=request.GET.get("term")).exclude(precio_compra=0)
        nombre = list()
        if producto:
            
            for n in producto:
                if n.stock > n.stock_min:
                    color = "badge-success"
                elif n.stock <= n.stock_min:
                    color = "badge-warning"
                else:
                    color = "badge-danger"
                
                dicProductos = {}
                dicProductos['id'] = n.id
                dicProductos['label'] = '<li style="font-size: 13px;" class="list-group-item d-flex justify-content-between align-items-center"><div class="col-sm-4">'+str(n.nombre)+'</div><span class="badge '+str(color)+' badge-pill text-white">'+str(n.stock)+'</span><span class="float-right">$'+str(n.precio_venta)+'</span></li>'
                dicProductos['value'] = n.nombre
                dicProductos['stock'] = n.stock
                dicProductos['codigo'] = n.codigo
                dicProductos['precio'] = n.precio_compra
                nombre.append(dicProductos)
            return JsonResponse(nombre, safe=False)
        else:
            dicProductos = {}
            dicProductos['n'] = 1
            dicProductos['label'] = '<li class="list-group-item align-items-center"><div class="col-sm-4"><span class="badge badge-pill badge-danger">Dar alta producto</span></div></li>'
            nombre.append(dicProductos)
            return JsonResponse(nombre, safe=False)

    
#Obtiene lista de proveedores
def proveedorAutocomplete(request):
   
    if 'term' in request.GET:

        proveedor = proveedores.objects.filter(nombre__icontains=request.GET.get("term"))
        nombre = list()
        if proveedor:
            for n in proveedor:
            
                
                dicProveedores = {}
            
                dicProveedores['label'] = n.nombre
                dicProveedores['condicion'] = n.condicion
                dicProveedores['cuit'] = n.cuit
            
                
                nombre.append(dicProveedores)
            return JsonResponse(nombre, safe=False)
        else:
            dicProveedores = {}
            dicProveedores['n'] = 1
            dicProveedores['label'] = '<li class="list-group-item align-items-center"><div class="col-sm-4"><span class="badge badge-pill badge-danger">Dar alta proveedor</span></div></li>'
            nombre.append(dicProveedores)
            return JsonResponse(nombre, safe=False)




#Registra las compras
@login_required
@permission_required('compras.add_compras', login_url='compras')
def cargarCompra(request):
   
    
    if request.is_ajax and request.method == "POST":
        
        
        form = comprasForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponse(True)
        else:
            data = {
                'error': form.errors.as_data()
            } 
           
            return JsonResponse({"error": list(data['error']['comprobante'][0])}, status = 400, safe = False)

  
        

#Carga el detalle de las compras realizadas
@login_required
@permission_required('compras.add_compras', login_url='compras')
def cargarDetalleCompra(request):
    usuario = request.user.username
 
    if request.is_ajax():
        data = {}

        ultima_compra = Compras.objects.order_by('id', 'fecha').last()
        id_producto = request.GET['id_producto']
        cantidad = request.GET['cantidad']
        precio = Producto.objects.get(id=id_producto)
        
        
        total = int(cantidad) * float(precio.precio_compra)
        
        neto = float(total) / 1.21
        iva = float(neto) * 0.21
        
        producto = Producto.objects.get(id=id_producto)

        data['id_compra'] = ultima_compra
        data['id_producto'] = id_producto
        data['cantidad'] = cantidad
        data['iva'] = "{0:.2f}".format(iva)
        data['subTotal'] = "{0:.2f}".format(neto)
        data['total'] = total
        
        tipoMov = "Compra"
        fecha = ultima_compra.fecha
        detalle = ""
        nombreProducto = producto.nombre
        
        
       
        formulario = detalleComprasForm(data)
        if formulario.is_valid():
            
            formulario.save()

            if id_producto:
                
                stockProducto = int(producto.stock) + int(cantidad)
                producto.stock = stockProducto
                producto.save()
                cargarStock(ultima_compra.id, tipoMov, fecha, detalle, cantidad, nombreProducto, stockProducto, usuario)
            messages.add_message(request, messages.SUCCESS, "La compra se confirmó exitosamente")

            return HttpResponse(True)
            
        

    return JsonResponse({"error": "Error"}, status=400)


#Mustra el detalle de una compra seleccionada
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




# @login_required
# def imprimir(request):
#     return render(request, 'compras/imprimir.html')


# def reporteCompras(request):

    
#     compra = detalleCompra.objects.values('id_compra__id', 'id_compra__comprobante', 'id_compra__cuit__nombre', 'id_compra__fecha').annotate(Sum('total'))


#     data = {
#         "compras": compra,
#         "fecha" : datetime.now()
#     }

#     pdf = render_pdf('compras/pdfCompras.html', data)

#     return HttpResponse(pdf, content_type='application/pdf')



#Muestra los pagos realizados y pendientes
@login_required
@permission_required('compras.view_compras', login_url='compras')
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
        dicPago = {}
        dicPago['id'] = d['id_compra__id']
        dicPago['comprobante'] = d['id_compra__comprobante']
        dicPago['fecha'] = d['id_compra__fecha']
        dicPago['nombre'] = d['id_compra__cuit__nombre']
        dicPago['total'] = d['total__sum']
        dicPago['saldo'] = total
        dicPago['estado'] = d['id_compra__estado']
        
        compratotal.append(dicPago)

    data = {
        "compras": compratotal
    }


    
    
    

    return render(request, 'compras/pagos.html', data)

#Registra un nuevo pago
@login_required
@permission_required('compras.add_compras', login_url='compras')
def registroPago(request):
    data= {
        "formPago": formPagoCompra()
        }

    if request.method == "POST":

        total = float(request.POST.get('total'))
        id_compra = request.POST.get('id_compra')
        tipoPago = request.POST.get('tipoPago')
        saldo = detalleCompra.objects.values('id_compra__comprobante').annotate(Sum('total')).filter(id_compra=id_compra)
     
        for c in saldo:
            comprobante = c['id_compra__comprobante']
            deuda = c['total__sum']

        pago = formaPagoCompra.objects.filter(id_compra=id_compra).annotate(Sum('total'))
        if pago:
            for p in pago:
                saldo = float(deuda) - float(p.total__sum) 
        else:
            saldo = float(deuda)
        
        if total <= float(saldo):
            
                
            caja_actual = Caja.objects.order_by('id', 'total', 'estado').last()
            
            if tipoPago == 'Efectivo':
                if caja_actual != None and caja_actual.estado:
                    
                    if caja_actual.total >= total:
                        cargarPago(id_compra, total, tipoPago, deuda)
                        #Registra el monto pagado en movimientos de la caja si es en efectivo y la caja se encuentra abierta
                        fecha = datetime.now()
                        caja = {}
                        caja['descripcion'] = "Compra comprobante N° " + comprobante
                        caja['operacion'] = 1
                        caja['monto'] = total
                        caja['id_caja'] = caja_actual.id
                        caja['saldo'] = deuda
                        caja['fecha'] = fecha
                        formulario = movimientoCajaForm(caja)
                            
                        if formulario.is_valid():
                            post = formulario.save(commit=False)
                        
                            ultimo_saldo = movCaja.objects.latest('fecha').saldo
                                
                            total = float(ultimo_saldo) - float(total)
                            post.saldo = total 
                            post.save()
                            caja_actual.total = total
                            caja_actual.save()
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


@login_required
@permission_required('compras.add_compras', login_url='compras')
def cargarPago(id_compra, total, tipoPago, deuda):
    #Registra el pago en formaPagoCompra 
    data = {}
    data['id_compra'] = id_compra
    data['fecha'] = datetime.now()
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
        
        
        compras = detalleCompra.objects.values('id_compra', 'id_compra__cuit__nombre', 'id_compra__fecha', 'id_compra__cuit', 'id_compra__estado').annotate(Sum('total')).filter(id_compra__cuit__nombre__icontains=request.GET.get("term"), id_compra__estado="Adeudado")
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


@login_required
@permission_required('compras.add_compras', login_url='compras')
def detallePago(request):
    
    return render(request, 'compras/detallePago.html')


@login_required
@permission_required('compras.add_compras', login_url='compras')
def reporteCompra(request):
    return render(request, 'compras/reporteCompras.html')


#Elmina la compra
@login_required
@permission_required('compras.delete_compras', login_url='compras')
def eliminarCompra(request, id):
    compra = get_object_or_404(Compras, pk=id)
    print(id)
    if compra:
        
        detalle = detalleCompra.objects.filter(id_compra = id).values('id_producto', 'cantidad')
        for d in detalle:
            producto = Producto.objects.get(id=d['id_producto'])
            
            stockProducto = int(producto.stock) - int(d['cantidad'])
            producto.stock = stockProducto
            producto.save()
            

        compra.delete()
        eliminarStock(id, tipo="Compra")
        messages.add_message(request, messages.SUCCESS, "La compra se eliminó exitosamente")
        return redirect(to='compras')
    

#Elimina el pago
@login_required
@permission_required('compras.delete_compras', login_url='compras')
def eliminarPago(request, id):
    pago = formaPagoCompra.objects.filter(id_compra=id)
    saldo = 0.0
    for p in pago:
        saldo = float(p.total)
        tipo = p.tipoPago

        if pago:
            
            if tipo == "Efectivo":
                caja_actual = Caja.objects.order_by('id', 'total', 'estado').last()
                fecha = datetime.now()
                caja = {}
                caja['descripcion'] = "Eliminacion pago "
                caja['operacion'] = 0
                caja['monto'] = saldo
                caja['id_caja'] = caja_actual.id
                caja['saldo'] = saldo
                caja['fecha'] = fecha
                formulario = movimientoCajaForm(caja)
                                
                if formulario.is_valid():
                    post = formulario.save(commit=False)
                            
                    ultimo_saldo = movCaja.objects.latest('fecha').saldo
                                    
                    total = float(ultimo_saldo) + float(saldo)
                    post.saldo = total 
                    post.save()
                    caja_actual.total = total
                    caja_actual.save()
                    
    pago.delete()

    compra = Compras.objects.get(id=id)
    compra.estado = "Adeudado"
    compra.save()

    return redirect(to='pago')


#Muestra el detalle del pago
@login_required
@permission_required('compras.view_compras', login_url='compras')
def detalleFormaPago(request):
    
    if request.is_ajax():
        id = request.POST.get("id")
        pago = formaPagoCompra.objects.filter(id_compra=id).values('id_compra__comprobante','total', 'tipoPago', 'fecha')
        
        return JsonResponse({"data": list(pago)})

    
    


