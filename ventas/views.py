from datetime import datetime
from django.contrib import messages
from django.db.models.aggregates import Sum
#from django.contrib.auth.decorators import login_required, permission_required
#from django.db.models.aggregates import Sum
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from caja.forms import cajaForm
from caja.models import Caja
from cedal.form import formPago
from cedal.models import formaPago
from clientes.models import Clientes
from producto.forms import ventaProductoForm
from producto.models import Producto
from ventas.forms import detalleVentaForm, ventasForm
from compras.utils import render_pdf
from django.views.generic import View

from ventas.models import Ventas, detalleVenta

from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO
import os
from django.conf import settings

from django.contrib.staticfiles import finders
# Create your views here.
# @login_required
# @permission_required('ventas.view_ventas', login_url='index')
def index(request):


    venta = detalleVenta.objects.values('id_venta__id', 'id_venta__comprobante', 'id_venta__cuit__nombre', 'id_venta__fecha').annotate(Sum('total'))

    #venta = Ventas.objects.all()
    data = {
        "ventas": venta
    }


    return render(request, 'ventas/ventas.html', data)


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
                signer_json['precio'] = n.precio_venta
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
        

        data['id_venta'] = ultima_venta
        data['id_producto'] = id_producto
        data['cantidad'] = cantidad
        data['iva'] = "{0:.2f}".format(iva)
        data['subTotal'] = "{0:.2f}".format(neto)
        data['total'] = total
        
        
        formulario = detalleVentaForm(data)
        if formulario.is_valid():
            
            formulario.save()

            if id_producto:
                producto = Producto.objects.get(id=id_producto)
                stock = int(producto.stock) - int(cantidad)
                producto.stock = stock
                producto.save()
            messages.add_message(request, messages.SUCCESS, "La venta se confirmó exitosamente")

            return HttpResponse(True)
            
        

    return JsonResponse({"error": "Error"}, status=400)


def detallesVenta(request, id):
    
    ventas = Ventas.objects.filter(id=id).select_related('cuit')
   
    data = {
        "datos": ventas
    }
    
    data["pagos"] = formaPago.objects.filter(id_venta=id).select_related('tipoDebito').select_related('tipoCredito')

    data["formPago"] = formPago()

    detalle = detalleVenta.objects.filter(id_venta=id).select_related('id_producto')
    
    iva = detalleVenta.objects.filter(id_venta=id).aggregate(Sum('iva'))
    subTotal = detalleVenta.objects.filter(id_venta=id).aggregate(Sum('subTotal'))
    total = detalleVenta.objects.filter(id_venta=id).aggregate(Sum('total'))
    
    
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

            data['id_venta'] = id
            

            pago = formPago(data)
        
            if pago.is_valid(): 
                pago.save()
                
                messages.add_message(request, messages.SUCCESS, "La forma de pago se realizo exitosamente")
            
            if efectivo > 0:
                
                caja = {}
                caja['descripcion'] = "Venta comprobante N° " + comprobante
                caja['operacion'] = 0
                caja['monto'] = efectivo 

                formulario = cajaForm(caja)

                if formulario.is_valid():
                    post = formulario.save(commit=False)
            
                    ultimo_saldo = Caja.objects.latest('fecha').saldo
                    
                    post.saldo = float(ultimo_saldo) + float(efectivo)
            
                    fecha = datetime.now()
                    post.fecha = fecha
                    post.save()
            else:
                data["formPago"] = formPago() 
        else:
            messages.add_message(request, messages.ERROR, "El monto seleccionado es diferente al monto total de la compra")
            return render(request, 'ventas/detalleVenta.html', data)
        

    return render(request, 'ventas/detalleVenta.html', data)


def reporteVentas(request, id):

    
    ventas = Ventas.objects.filter(id=id).select_related('cuit')
    
    data = {
        "datos": ventas
    }
    
    data["pagos"] = formaPago.objects.filter(id_venta=id).select_related('tipoDebito').select_related('tipoCredito')

    data["formPago"] = formPago()

    detalle = detalleVenta.objects.filter(id_venta=id).select_related('id_producto')
    
    iva = detalleVenta.objects.filter(id_venta=id).aggregate(Sum('iva'))
    subTotal = detalleVenta.objects.filter(id_venta=id).aggregate(Sum('subTotal'))
    total = detalleVenta.objects.filter(id_venta=id).aggregate(Sum('total'))

    
    data["iva"] = iva
    data["subTotal"] = subTotal
    data["total"] = total
        
    data["detalles"] = detalle
    datos ={}

    pdf = render_pdf('ventas/imprimirVenta.html', datos)

    return HttpResponse(pdf, content_type='application/pdf')


class VentasPdf(View):

    def link_callback(self, uri, rel):
        
        result = finders.find(uri)
        if result:
                if not isinstance(result, (list, tuple)):
                        result = [result]
                result = list(os.path.realpath(path) for path in result)
                path=result[0]
        else:
                sUrl = settings.STATIC_URL        # Typically /static/
                sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                mUrl = settings.MEDIA_URL         # Typically /media/
                mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                if uri.startswith(mUrl):
                    path = os.path.join(mRoot, uri.replace(mUrl, ""))
                elif uri.startswith(sUrl):
                    path = os.path.join(sRoot, uri.replace(sUrl, ""))
                else:
                    return uri

            # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                    'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
        return path

    def get(self, request, *args, **kwargs):

        ventas = Ventas.objects.filter(id=self.kwargs['id']).select_related('cuit')
    
        data = {
            "datos": ventas
        }
        
        data["pagos"] = formaPago.objects.filter(id_venta=self.kwargs['id']).select_related('tipoDebito').select_related('tipoCredito')

        data["formPago"] = formPago()

        detalle = detalleVenta.objects.filter(id_venta=self.kwargs['id']).select_related('id_producto')
        
        iva = detalleVenta.objects.filter(id_venta=self.kwargs['id']).aggregate(Sum('iva'))
        subTotal = detalleVenta.objects.filter(id_venta=self.kwargs['id']).aggregate(Sum('subTotal'))
        total = detalleVenta.objects.filter(id_venta=self.kwargs['id']).aggregate(Sum('total'))

        
        data["iva"] = iva
        data["subTotal"] = subTotal
        data["total"] = total
            
        data["detalles"] = detalle

        data['direccion'] = 'entre rios 124'
        data['localidad'] = 'Rio Ceballos'
        data['provincia'] = 'Cordoba'

        template = get_template('ventas/pdfVentas.html')
        context = {'title': 'Mi primer pdf'}
        html = template.render(data)
        response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'
        pisaStatus = pisa.CreatePDF(html, dest=response)
        if pisaStatus.err:
            return HttpResponse("asdads" + html + 'asddd')
        
        return response
