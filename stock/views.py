from django.shortcuts import render
from django.http import JsonResponse
from producto.models import Producto
from stock.forms import ajusteForm, detalleAjusteForm
from django.http import HttpResponse
from datetime import datetime
from stock.models import ajusteStock, stock

from django.contrib import messages
# Create your views here.

def altaAjuste(request):

    # data = {
    #     "form": ajusteForm()
    # }
    

    return render(request, 'stock/ajuste.html')

def productoAuto(request):
   
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
                signer_json['precio'] = n.precio_compra
                nombre.append(signer_json)
            return JsonResponse(nombre, safe=False)
        else:
            signer_json = {}
            signer_json['n'] = 1
            signer_json['label'] = '<li class="list-group-item align-items-center"><div class="col-sm-4"><span class="badge badge-pill badge-danger">Dar alta producto</span></div></li>'
            nombre.append(signer_json)
            return JsonResponse(nombre, safe=False)


def cargarAjuste(request):
   
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        data = {}

        usuario = request.user.username
        detalle = request.POST['detalle']

    
        data['fecha'] = datetime.now()
        data['detalle'] = detalle
        data['usuario'] = usuario
        # get the form data
        form = ajusteForm(data)
        # save the data and after fetch the object in instance
        if form.is_valid():
            form.save()
            #ultima_compra = Compras.objects.order_by('id', 'fecha').last()
            return HttpResponse(True)
            

    # some error occured
    return JsonResponse({"error": "Error"}, status=400)


def cargarDetalleAjuste(request):

    if request.is_ajax():
        data = {}

        ultimo_ajuste = ajusteStock.objects.order_by('id', 'fecha').last()
        id_producto = request.GET['id_producto']
        cantidad = request.GET['stockNuevo']
    
        data['id_ajuste'] = ultimo_ajuste
        data['id_producto'] = id_producto
        data['stock_nuevo'] = cantidad
        
        
        formulario = detalleAjusteForm(data)
        print(formulario)
        if formulario.is_valid():
            
            formulario.save()

            if id_producto:
                producto = Producto.objects.get(id=id_producto)
                producto.stock = cantidad
                producto.save()
            messages.add_message(request, messages.SUCCESS, "La compra se confirmó exitosamente")

            return HttpResponse(True)
            
        

    return JsonResponse({"error": "Error"}, status=400)