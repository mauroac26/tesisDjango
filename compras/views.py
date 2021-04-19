from django.shortcuts import render, redirect
from .forms import comprasForm
from producto.forms import productoForm, compraProductoForm
from .models import Compras
from proveedores.forms import proveedorCompraForm
from producto.models import Producto
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request, 'compras/compras.html')

def altaCompra(request):

    data = {
        "form": compraProductoForm()
    }

    data["formCompra"] = comprasForm()

    data["formProveedor"] = proveedorCompraForm()

    # if request.method == "POST":
        # formulario = productoForm(data=request.POST)
        # if formulario.is_valid():   
            
        #     #data["mensaje"] = choice
        #     return redirect(to='compras')
        # else:
        #     data["form"] = formulario

    return render(request, 'compras/altaCompra.html', data)


def productoAutocomplete(request):
   
    if 'term' in request.GET:

        producto = Producto.objects.filter(nombre__icontains=request.GET.get("term"))
        nombre = list()
        for n in producto:
            signer_json = {}
            signer_json['id'] = n.id
            signer_json['label'] = n.nombre
            signer_json['stock'] = n.stock
            signer_json['codigo'] = n.codigo
            signer_json['precio'] = n.precio_compra
            nombre.append(signer_json)
        return JsonResponse(nombre, safe=False)
    # return HttpResponse(data, 'compras/altaCompra.html')
    return render(request, 'compras/altaCompra.html')
