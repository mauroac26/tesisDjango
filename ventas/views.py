from datetime import date, datetime
from django.contrib import messages
from django.db.models.aggregates import Sum
from django.contrib.auth.decorators import login_required, permission_required
from xhtml2pdf import pisa
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from caja.forms import movCajaForm, movimientoCajaForm
from caja.models import Caja, movCaja
from clientes.models import Clientes
from producto.forms import ventaProductoForm
from producto.models import Producto, ProductoPromocion
from stock.views import cargarStock
from ventas.forms import detalleVentaForm, formPagoVenta, ventasForm
from compras.utils import render_pdf
from django.views.generic import View
from cedal.views import consultaPromo
from ventas.models import Ventas, detalleVenta, formaPagoVenta


from django.template.loader import get_template
import os
from django.conf import settings


# Create your views here.
# @login_required
# @permission_required('ventas.view_ventas', login_url='index')
def index(request):

    consultaPromo()

    venta = detalleVenta.objects.values('id_venta__id', 'id_venta__comprobante', 'id_venta__cuit__nombre', 'id_venta__fecha').annotate(Sum('total'))
    
    #venta = Ventas.objects.all()
    data = {
        "ventas": venta
    }


    return render(request, 'ventas/ventas.html', data)

@login_required
@permission_required('ventas.add_ventas', login_url='ventas')
def altaVenta(request):

    data = {
        "form": ventaProductoForm()
    }

    data["formVenta"] = ventasForm()


    return render(request, 'ventas/altaVenta.html', data)


def clienteAutocomplete(request):
   
    if 'term' in request.GET:

        proveedor = Clientes.objects.filter(nombre__icontains=request.GET.get("term"))
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
            signer_json['label'] = '<li class="list-group-item align-items-center"><div class="col-sm-4"><span class="badge badge-pill badge-danger">Dar alta cliente</span></div></li>'
            nombre.append(signer_json)
            return JsonResponse(nombre, safe=False)


def productoVentaAutocomplete(request):
    descuento = 0
    if 'term' in request.GET:

        producto = Producto.objects.filter(nombre__icontains=request.GET.get("term"))
        nombre = list()
        hoy =  date(datetime.now().year, datetime.now().month, datetime.now().day)
        if producto:
            
            for n in producto:
                # vencimiento = n.vencimiento
                # fecha = date(vencimiento.year, vencimiento.month, vencimiento.day)
                # resultado = hoy - fecha
                if n.stock > n.stock_min:
                    color = "badge-success"
                elif n.stock <= n.stock_min:
                    color = "badge-warning"
                else:
                    color = "badge-danger"
                
                promocion = ProductoPromocion.objects.filter(id_producto=n.id)
                if promocion:
                    for p in promocion:
                        descuento = p.descuento
                

                signer_json = {}
                signer_json['id'] = n.id
                signer_json['label'] = '<li class="list-group-item d-flex justify-content-between align-items-center"><div class="col-sm-4">'+str(n.nombre)+'</div><span class="badge '+str(color)+' badge-pill text-white">'+str(n.stock)+'</span><span class="float-right">$'+str(n.precio_venta)+'</span></li>'
                signer_json['value'] = n.nombre
                signer_json['stock'] = n.stock
                signer_json['codigo'] = n.codigo
                signer_json['precio'] = n.precio_venta
                signer_json['descuento'] = descuento
                # signer_json['vencimiento'] = resultado.days
                nombre.append(signer_json)
            return JsonResponse(nombre, safe=False)
        else:
            signer_json = {}
            signer_json['n'] = 1
            signer_json['label'] = '<li class="list-group-item align-items-center"><div class="col-sm-4"><span class="badge badge-pill badge-danger">Dar alta producto</span></div></li>'
            nombre.append(signer_json)
            return JsonResponse(nombre, safe=False)



def cargarVenta(request):
   
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        
        # get the form data
        form = ventasForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            form.save()
            #ultima_compra = Compras.objects.order_by('id', 'fecha').last()
            return HttpResponse(True)
            

    # some error occured
    return JsonResponse({"error": "ingresar comprobante valido"}, status=400)


def cargarDetalleVenta(request):

    if request.is_ajax():
        data = {}

        ultima_venta = Ventas.objects.order_by('id', 'fecha').last()
        id_producto = request.GET['id_producto']
        cantidad = request.GET['cantidad']
        precio = Producto.objects.get(id=id_producto)
        
        
        total = int(cantidad) * float(precio.precio_venta)
        
        neto = float(total) / 1.21
        iva = float(neto) * 0.21
        
        producto = Producto.objects.get(id=id_producto)

        data['id_venta'] = ultima_venta
        data['id_producto'] = id_producto
        data['cantidad'] = cantidad
        data['iva'] = "{0:.2f}".format(iva)
        data['subTotal'] = "{0:.2f}".format(neto)
        data['total'] = total
        
        tipoMov = "Venta"
        fecha = ultima_venta.fecha
        detalle = ""
        nombreProducto = producto.nombre
        
        usuario = request.user.username
        
        formulario = detalleVentaForm(data)
        if formulario.is_valid():
            
            formulario.save()

            if id_producto:
                
                stockProducto = int(producto.stock) - int(cantidad)
                producto.stock = stockProducto
                producto.save()
                cargarStock(tipoMov, fecha, detalle, cantidad, nombreProducto, stockProducto, usuario)
            messages.add_message(request, messages.SUCCESS, "La venta se confirmó exitosamente")

            return HttpResponse(True)
            
        

    return JsonResponse({"error": "Error"}, status=400)


def detallesVenta(request, id):
    
    ventas = Ventas.objects.filter(id=id).select_related('cuit')
   
    data = {
        "datos": ventas
    }
    
    # data["pagos"] = formaPago.objects.filter(id_venta=id).select_related('tipoDebito').select_related('tipoCredito')

    # data["formPago"] = formPago()

    detalle = detalleVenta.objects.filter(id_venta=id).select_related('id_producto')
    
    iva = detalleVenta.objects.filter(id_venta=id).aggregate(Sum('iva'))
    subTotal = detalleVenta.objects.filter(id_venta=id).aggregate(Sum('subTotal'))
    total = detalleVenta.objects.filter(id_venta=id).aggregate(Sum('total'))
    
    data['id_venta'] = id
    
    
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
            
            data['id_venta'] = id
            data['efectivo'] = efectivo
            data['credito'] = credito
            data['debito'] = debito
            data['cuotas'] = cuotas
            data['tipoCredito'] = tipoCredito
            data['tipoDebito'] = tipoDebito

            

            # pago = formPago(data)
        
            # if pago.is_valid(): 
            #     pago.save()
                
            #     messages.add_message(request, messages.SUCCESS, "La forma de pago se realizo exitosamente")
            
            if efectivo > 0:
                
                caja = {}
                caja['descripcion'] = "Venta comprobante N° " + comprobante
                caja['operacion'] = 0
                caja['monto'] = efectivo 

                formulario = movCajaForm(caja)

                if formulario.is_valid():
                    post = formulario.save(commit=False)
            
                    ultimo_saldo = movCaja.objects.latest('fecha').saldo
                    
                    post.saldo = float(ultimo_saldo) + float(efectivo)
            
                    fecha = datetime.now()
                    post.fecha = fecha
                    post.save()
            else:
                data["formPago"] = formPagoVenta() 
        else:
            messages.add_message(request, messages.ERROR, "El monto seleccionado es diferente al monto total de la compra")
            return render(request, 'ventas/detalleVenta.html', data)
        

    return render(request, 'ventas/detalleVenta.html', data)


# def reporteVentas(request, id):

    
#     ventas = Ventas.objects.filter(id=id).select_related('cuit')
    
#     data = {
#         "datos": ventas
#     }
    
#     data["pagos"] = formaPago.objects.filter(id_venta=id).select_related('tipoDebito').select_related('tipoCredito')

#     data["formPago"] = formPago()

#     detalle = detalleVenta.objects.filter(id_venta=id).select_related('id_producto')
    
#     iva = detalleVenta.objects.filter(id_venta=id).aggregate(Sum('iva'))
#     subTotal = detalleVenta.objects.filter(id_venta=id).aggregate(Sum('subTotal'))
#     total = detalleVenta.objects.filter(id_venta=id).aggregate(Sum('total'))

    
#     data["iva"] = iva
#     data["subTotal"] = subTotal
#     data["total"] = total
        
#     data["detalles"] = detalle
#     datos ={}

#     pdf = render_pdf('ventas/imprimirVenta.html', datos)

#     return HttpResponse(pdf, content_type='application/pdf')


# class VentasPdf(View):

#     def link_callback(self, uri, rel):
        
    
        
#         sUrl = settings.STATIC_URL        # Typically /static/
#         sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
#         mUrl = settings.MEDIA_URL         # Typically /media/
#         mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

#         if uri.startswith(mUrl):
#             path = os.path.join(mRoot, uri.replace(mUrl, ""))
#         elif uri.startswith(sUrl):
#             path = os.path.join(sRoot, uri.replace(sUrl, ""))
#         else:
#             return uri

#             # make sure that file exists
#         if not os.path.isfile(path):
#             raise Exception(
#                     'media URI must start with %s or %s' % (sUrl, mUrl)
#                     )
#         return path

#     def get(self, request, *args, **kwargs):

#         ventas = Ventas.objects.filter(id=self.kwargs['id']).select_related('cuit')
    
#         data = {
#             "datos": ventas
#         }
        
#         data["pagos"] = formaPago.objects.filter(id_venta=self.kwargs['id']).select_related('tipoDebito').select_related('tipoCredito')

#         data["formPago"] = formPago()

#         detalle = detalleVenta.objects.filter(id_venta=self.kwargs['id']).select_related('id_producto')
        
#         iva = detalleVenta.objects.filter(id_venta=self.kwargs['id']).aggregate(Sum('iva'))
#         subTotal = detalleVenta.objects.filter(id_venta=self.kwargs['id']).aggregate(Sum('subTotal'))
#         total = detalleVenta.objects.filter(id_venta=self.kwargs['id']).aggregate(Sum('total'))

        
#         data["iva"] = iva
#         data["subTotal"] = subTotal
#         data["total"] = total
#         data['id_venta'] = self.kwargs['id']
#         data["detalles"] = detalle
        
#         data['direccion'] = 'Ruta E53 km 18'
#         data['localidad'] = 'Río Ceballos'
#         data['provincia'] = 'Córdoba'
#         data['icono'] = '{}{}'.format(settings.MEDIA_URL, 'cedal.png')


#         template = get_template('ventas/pdfVentas.html')
        
#         html = template.render(data)
#         response = HttpResponse(content_type='application/pdf')
#         #response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'
#         pisaStatus = pisa.CreatePDF(html, dest=response, link_callback=self.link_callback)
#         if pisaStatus.err:
#             return HttpResponse("asdads" + html + 'asddd')
        
#         return response


def pagoVenta(request):
    venta = detalleVenta.objects.values('id_venta__id', 'id_venta__comprobante', 'id_venta__cuit__nombre', 'id_venta__fecha', 'id_venta__estado').annotate(Sum('total'))

    ventaTotal = list()

    data = {
        "ventas": venta
    }

    for d in data["ventas"]:
        pago = formaPagoVenta.objects.filter(id_venta=d['id_venta__id']).annotate(Sum('total'))
        saldo = 0
        for p in pago:
            saldo = float(p.total__sum) + saldo
            
        total = float(d['total__sum']) - saldo
        signer_json = {}
        signer_json['id'] = d['id_venta__id']
        signer_json['comprobante'] = d['id_venta__comprobante']
        signer_json['fecha'] = d['id_venta__fecha']
        signer_json['nombre'] = d['id_venta__cuit__nombre']
        signer_json['total'] = d['total__sum']
        signer_json['saldo'] = total
        signer_json['estado'] = d['id_venta__estado']
        
        ventaTotal.append(signer_json)

    data = {
        "ventas": ventaTotal
    }


    
    
    

    return render(request, 'ventas/pagoVenta.html', data)


def ventaAdeudada(request):
    if 'term' in request.GET:
        
        ventas = detalleVenta.objects.values('id_venta__cuit__nombre', 'id_venta__fecha','id_venta').annotate(Sum('total')).filter(id_venta__cuit__nombre__icontains=request.GET.get("term"), id_venta__estado = 'Adeudado')
        
        nombre = list()
        if ventas:
            for n in ventas:
                pago = formaPagoVenta.objects.filter(id_venta=n['id_venta']).annotate(Sum('total'))
                saldo = 0.0
                for p in pago:
                    saldo = float(p.total__sum) + float(saldo)
            
                total = float(n['total__sum']) - float(saldo)
                
                # fecha = n['id_venta__fecha']
                # fecha1 = datetime.datetime.strptime(fecha, '%Y-%m-%dT%H:%MZ').strftime("%d-%m-%Y")
                dicventas = {}
                dicventas['id'] = n['id_venta']
                dicventas['label'] = '<li style="font-size: 11px;" class="list-group-item d-flex justify-content-between align-items-center"><div class="col-sm-5">'+str(n['id_venta__cuit__nombre'])+'</div><span>'+str(n['id_venta__fecha'])+'</span><span>$'+str(n['total__sum'])+'</span></li>'
                dicventas['value'] = f'{n["id_venta__cuit__nombre"]} / {n["id_venta__fecha"]} / {n["total__sum"]}'
                dicventas['total'] = float(total)
                
                nombre.append(dicventas)
            return JsonResponse(nombre, safe=False)
        else:
            dicventas = {}
            dicventas['n'] = 1
            dicventas['label'] = '<li style="font-size: 11px;" class="list-group-item align-items-center"><div class="col-sm-7"><span>No se encuentas ventas adeudadas</span></div></li>'
            nombre.append(dicventas)
            return JsonResponse(nombre, safe=False)


def registroPagoVenta(request):
    data= {
        "formPago": formPagoVenta()
        }

    if request.method == "POST":

        total = float(request.POST.get('total'))
        id_venta = request.POST.get('id_venta')
        tipoPago = request.POST.get('tipoPago')
        tarjeta = request.POST.get('tipoCredito')
        cuotas = request.POST.get('cuotas')
     
        ven = detalleVenta.objects.values('id_venta__comprobante').annotate(Sum('total')).filter(id_venta=id_venta)
        for c in ven:
            comprobante = c['id_venta__comprobante']
            deuda = c['total__sum']
        
        pago = formaPagoVenta.objects.filter(id_venta=id_venta).annotate(Sum('total'))
        if pago:
            for p in pago:
                saldo = float(deuda) - float(p.total__sum) 
        else:
            saldo = float(deuda)
        
        
        if total <= float(saldo):
            
                
            caja_actual = Caja.objects.order_by('id', 'total', 'estado').last()
            
            if tipoPago == 'Efectivo':
                if caja_actual.estado:
                    
                    cargarPagoVenta(id_venta, total, tipoPago, deuda, tarjeta, cuotas)
                    #Registra el monto pagado en movimientos de la caja si es en efectivo y la caja se encuentra abierta
                    fecha = datetime.now()
                    caja = {}
                    caja['descripcion'] = "Venta comprobante N° " + comprobante
                    caja['operacion'] = 0
                    caja['monto'] = total
                    caja['id_caja'] = caja_actual.id
                    caja['saldo'] = deuda
                    caja['fecha'] = fecha
                    formulario = movimientoCajaForm(caja) 
                            
                    if formulario.is_valid():
                        post = formulario.save(commit=False)
                        
                        ultimo_saldo = movCaja.objects.latest('fecha').saldo
                                
                        total = float(ultimo_saldo) + float(total)
                        post.saldo = total
                        post.save()
                        caja_actual.total = total
                        caja_actual.save()
                        messages.add_message(request, messages.SUCCESS, "La forma de pago se realizo exitosamente")
                        return redirect(to='pagoVenta')
                    else:
                        data["formPago"] = formulario
                    
                else:
                    messages.add_message(request, messages.ERROR, "No se puede realizar el pago, la caja se encuentra cerrada")
                    return redirect(to='registroPagoVenta')
            else:
                cargarPagoVenta(id_venta, total, tipoPago, deuda, tarjeta, cuotas)
                return redirect(to='pagoVenta')
                
        else:
            messages.add_message(request, messages.ERROR, "El monto seleccionado es mayor al monto total de la compra")
            return redirect(to='registroPagoVenta') 
    return render(request, 'ventas/registroPagoVenta.html', data)


def cargarPagoVenta(id_venta, total, tipoPago, deuda, tarjeta, cuotas):
    #Registra el pago en formaPagoCompra
     
    data = {}
    data['id_venta'] = id_venta
    data['fecha'] = datetime.now()
    data['total'] = total
    data['tipoPago'] = tipoPago
    data['cuotas'] = cuotas
    data['tipoCredito'] = tarjeta
    pago = formPagoVenta(data)
            
    if pago.is_valid(): 
        pago.save()
        #una vez registrado el pago compara si quedan deudas entre el monto pagado y el saldo total de la compra
        venta = Ventas.objects.get(id=id_venta)
        pago = formaPagoVenta.objects.filter(id_venta=id_venta).annotate(Sum('total'))
        tot = 0.0
        for p in pago:
            tot = float(p.total__sum) + float(tot)

        print(tot)     
        #si es igual el total y la deuda el estado de la venta pasa a pagado sino sigue estando en adeudado
        if float(tot) == float(deuda):
            venta.estado = 'Pagado'
            venta.save()


def detalleFormaPagoVenta(request):
    
    if request.is_ajax():
        id = request.POST.get("id")
        pago = formaPagoVenta.objects.filter(id_venta=id).values('id_venta__comprobante','total', 'tipoPago', 'fecha', 'cuotas', 'tipoCredito_id__nombre')
        
        return JsonResponse({"data": list(pago)})


def eliminarPagoVenta(request, id):
    pago = formaPagoVenta.objects.filter(id_venta=id)
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
                caja['operacion'] = 1
                caja['monto'] = saldo
                caja['id_caja'] = caja_actual.id
                caja['saldo'] = saldo
                caja['fecha'] = fecha
                formulario = movimientoCajaForm(caja)
                                
                if formulario.is_valid():
                    post = formulario.save(commit=False)
                            
                    ultimo_saldo = movCaja.objects.latest('fecha').saldo
                                    
                    total = float(ultimo_saldo) - float(saldo)
                    post.saldo = total 
                    post.save()
                    caja_actual.total = total
                    caja_actual.save()
                    
    pago.delete()

    obj = Ventas.objects.get(id=id)
    obj.estado = "Adeudado"
    obj.save()

    return redirect(to='pagoVenta')



def eliminarVenta(request, id):
    venta = get_object_or_404(Ventas, pk=id)
    
    if venta:
        detalle = detalleVenta.objects.filter(id_venta = id).values('id_producto', 'cantidad')
        for d in detalle:
            producto = Producto.objects.get(id=d['id_producto'])
            stockProducto = int(producto.stock) + int(d['cantidad'])
            producto.stock = stockProducto
            producto.save()
            

        venta.delete()
        messages.add_message(request, messages.SUCCESS, "La venta se eliminó exitosamente")
        return redirect(to='ventas')