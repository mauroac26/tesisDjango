
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from produccion.forms import produccionForm
from produccion.models import Produccion
from producto.models import Producto
from stock.views import cargarStock
from datetime import datetime
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

    # data["form"]["producto_retiro"] = data["form"]["producto_retiro"][1]
    # print(data["form"]["producto_retiro"][1].tag)

    if request.method == "POST":

        fecha = request.POST.get('fecha')
        producto_retiro = request.POST.get('producto_retiro')
        cantidad_retiro = request.POST.get('cantidad_retiro')
        producto_pedido = request.POST.get('producto_pedido')
        cantidad_pedido = request.POST.get('cantidad_pedido')
        detalle = ""
        usuario = request.user.username
        
        tipoMov = "Retiro para produccion"
        
        prodStock = Producto.objects.get(id=producto_retiro)
        nombreProducto = prodStock.nombre
        stock = int(prodStock.stock)
        
        if stock > 0 and int(cantidad_retiro) <= stock:

            formulario = produccionForm(data=request.POST)

            if formulario.is_valid():
                prod = formulario.save(commit=False)
                prod.usuario_id = request.user.id
                prod.save()
                
                stockProducto = stock - int(cantidad_retiro)
                prodStock.stock = stockProducto
                prodStock.save()
                cargarStock(tipoMov, fecha, detalle, cantidad_retiro, nombreProducto, stockProducto, usuario)

                prodStock = Producto.objects.get(id=producto_pedido)
                nombreProducto = prodStock.nombre
                stock = int(prodStock.stock)
                stockProducto = stock + int(cantidad_pedido)
                prodStock.stock = stockProducto
                prodStock.save()
                tipoMov = "Producto Producido"
                cargarStock(tipoMov, fecha, detalle, cantidad_pedido, nombreProducto, stockProducto, usuario)
                return redirect(to='produccion')
            else:
                data["form"] = formulario

        else:
            messages.add_message(request, messages.ERROR,  "no hay stock o no hay la cantidad deseada del producto seleccionado")
            

    return render(request, 'produccion/altaProduccion.html', data)


def eliminarProduccion(request, id):
    produccion = get_object_or_404( Produccion, pk=id)

    if produccion:
        producto = Producto.objects.get(id = produccion.producto_retiro_id)
        stockProducto = int(produccion.cantidad_retiro) + int(producto.stock) 
        producto.stock = stockProducto
        producto.save()
        produccion.delete()
        messages.add_message(request, messages.SUCCESS, "La produccion se eliminó exitosamente")
        return redirect(to='produccion')


def pedido(request):

    pedido = Produccion.objects.filter(fecha=datetime.now())

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
        detalle = ""
        usuario = request.user.username
        tipoMov = "Producto Producido"
        

        pedido = Produccion.objects.get(id = id_pedido)
        fecha = pedido.fecha
        pedido.estado = 'Producido'
        pedido.save()

        prod = Producto.objects.get(id=producto)
        nombreProducto = prod.nombre
        stockProducto = int(cantidad)  + int(prod.stock) 
        prod.stock = stockProducto
        prod.save()
        cargarStock(tipoMov, fecha, detalle, cantidad, nombreProducto, stockProducto, usuario)
        return redirect(to='pedido')
 