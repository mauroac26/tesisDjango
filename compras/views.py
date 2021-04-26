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
# Create your views here.
def index(request):
    return render(request, 'compras/compras.html')


def altaCompra(request):

    data = {
        "form": compraProductoForm()
    }

    data["formCompra"] = comprasForm()

    
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
    
    return render(request, 'compras/altaCompra.html')

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
        
        print(data)
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



# def prueba(request):
  
#     if request.is_ajax():
    
    
#         data = {}

#         ultima_compra = Compras.objects.order_by('id', 'fecha').last()
            
#         data['id_compra'] = ultima_compra
#         data['cantidad'] = request.GET['cantidad']
#         data['id_producto'] = request.GET['id_producto']

        
#         #data={}
        
#         # data['id_compra'] = request.GET['id_compra']
#         # data['id_producto'] = request.GET['id_producto']
#         # data['cantidad'] = request.GET['cantidad']
        

        
        
#             # data['id_compra'] = request.GET['id_compra']
#             # data['id_producto'] = request.GET['id_producto']
#             # data['cantidad'] = request.GET['cantidad']
        
#         formulario = detalleComprasForm(data)
        
#         if formulario.is_valid():
#             formulario.save()
#             return redirect(to='compras')
#         else:
#             return redirect(to='productos')
#     # if request.is_ajax():
        
#     #     id_compra = request.POST.get('id_compra')
#     #     id_producto = request.POST.get('id_producto')
#     #     cantidad = request.POST.get('cantidad')
        
#     #     lista = list()

#     #     data = {}

#     #     data['id_compra'] = id_compra
#     #     data['id_prducto'] = id_producto
#     #     data['cantidad'] = cantidad
        
#     #     form = lista.append(data)
#     #     formulario = detalleComprasForm(form)
#     #     if formulario.is_valid():
#     #         formulario.save()
#     #         return redirect(to='compras')
#     #     else:
#     #         return redirect(to='productos')
#         # lista = []

#         # data = {}
#         # data['id'] = "mauro"
#         # data['num'] = 1

#         #lista.append(data)

#         # datalista = json.dumps(form)
        
#         # return HttpResponse(datalista, 'compras/prueba.html')
     
#         # data={
#         #     "form": form
#         # }
#         # return render(request, 'compras/prueba.html', data)
#     else:
#         return render(request, 'compras/altaCompra.html')
    
   
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
    return JsonResponse({"error": ""}, status=400)


def cargarDetalleCompra(request):

    if request.is_ajax():
        data = {}

        ultima_compra = Compras.objects.order_by('id', 'fecha').last()
        id_producto = request.GET['id_producto']
        cantidad = request.GET['cantidad']
        

        data['id_compra'] = ultima_compra
        data['id_producto'] = id_producto
        data['cantidad'] = cantidad
        
        formulario = detalleComprasForm(data)
        if formulario.is_valid():
            
            formulario.save()
            return HttpResponse(True)
    return JsonResponse({"error": ""}, status=400)