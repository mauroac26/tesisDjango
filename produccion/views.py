
from django.shortcuts import redirect, render
from django.contrib import messages
from produccion.forms import produccionForm
from produccion.models import Produccion
from producto.models import Producto


# Create your views here.
def index(request):

    produccion = Produccion.objects.all()

    data = {
        "produccion": produccion
    }

    return render(request, 'produccion/produccion.html', data) 


def altaProduccion(request):

    # id = request.user.id
    # usuario = get_object_or_404(Users, pk=id)
    data = {
        "form": produccionForm()
    }

    # print(data["form"]["usuario"][1])

    if request.method == "POST":

        # fecha = request.POST.get('fecha')
        producto = request.POST.get('producto_retiro')
        cantidad = request.POST.get('cantidad_retiro')
        # usuario = request.POST.get('usuario')
        
        # data['fecha'] = fecha
        
        # data['cantidad'] = cantidad
        # data['producto'] = 1
        # data['usuario'] = usuario
        prod = Producto.objects.get(id=producto)
        stock = int(prod.stock)
        
        if stock > 0 and int(cantidad) <= stock:

            formulario = produccionForm(data=request.POST)

            if formulario.is_valid():
                formulario.save()
                
                
                stock = stock - int(cantidad)
                prod.stock = stock
                prod.save()
                
                return redirect(to='produccion')
            else:
                data["form"] = formulario

        else:
            messages.add_message(request, messages.ERROR,  "no hay stock o no hay la cantidad deseada del producto seleccionado")
            

    return render(request, 'produccion/altaProduccion.html', data)


def pedido(request):

    pedido = Produccion.objects.all()

    data = {
        "pedido": pedido
    }

    return render(request, 'produccion/pedido.html', data) 


# def altaPedido(request):

#     data = {
#         "form": pediodosForm()
#     }

#     if request.method == "POST":
#         formulario = pediodosForm(data=request.POST)
#         if formulario.is_valid():
#             formulario.save()
                
#             return redirect(to='pedido')
#         else:
#             data["form"] = formulario
        
#     return render(request, 'produccion/altaPedido.html', data) 


def producido(request):

    if request.is_ajax():
        # data = {}
        cantidad = request.GET['cantidad']
        producto = request.GET['id_Producto']
        id_pedido = request.GET['id']
        
        pedido = Produccion.objects.get(id = id_pedido)

        pedido.estado = 'Producido'
        pedido.save()

        prod = Producto.objects.get(id=producto)
        stock = int(cantidad)  + int(prod.stock) 
        prod.stock = stock
        prod.save()

        return redirect(to='pedido')
 