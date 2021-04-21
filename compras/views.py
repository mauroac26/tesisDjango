from django.shortcuts import render, redirect
from .forms import comprasForm
from producto.forms import productoForm, compraProductoForm
from .models import Compras
from proveedores.forms import proveedorCompraForm
from producto.models import Producto
from django.http import JsonResponse
from proveedores.models import proveedores
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


def cargarCompra(request):
    data = {}
    
    if request.method == "POST":
        formulario = comprasForm(data=request.POST)
        if formulario.is_valid(): 
            formulario.save()
            
            return redirect(to='compras')
            
        else:
            data["formCompra"] = formulario
       
        



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

