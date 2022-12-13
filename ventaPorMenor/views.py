from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse, JsonResponse
from producto.models import Producto
from ventaPorMenor.forms import detalleVentaPorMenorForm, ventaPorMenorForm
from .models import DetalleventaPorMenor, ventaPorMenor
from datetime import datetime
from django.contrib import messages
from stock.views import cargarStock, eliminarStock

# Create your views here.
def index(request):

    pedidoVenta = DetalleventaPorMenor.objects.all().values('producto__nombre', 'cantidad', 'id_ventaPorMenor__fecha', 'id_ventaPorMenor__usuario__username')
    pedidoVenta = ventaPorMenor.objects.all()
    data = {
        "pedidoVenta": pedidoVenta
    }

    return render(request, 'ventaPorMenor/ventaPorMenor.html', data) 


def altaRetiroPorMenor(request):


    data = {
        "form": detalleVentaPorMenorForm()
    }


    return render(request, 'ventaPorMenor/retiroVentaPorMenor.html', data)


def cargarRetiroVenta(request):
   
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        
        # get the form data
        data = {}

        data['fecha'] = datetime.now()
        data['usuario'] = request.user.id

        formulario = ventaPorMenorForm(data)

        if formulario.is_valid():
            
            formulario.save()
            return HttpResponse(True)
        messages.add_message(request, messages.ERROR, "Error en el registro")
        return JsonResponse({"error": "Error"}, status=400)
            

    # some error occured
    return JsonResponse({"error": "Error"}, status=400)


def cargarDetalleRetiroVenta(request):

    if request.is_ajax():
    
        data = {}

        ultimo_pedido = ventaPorMenor.objects.order_by('id', 'fecha').last()
        id_producto = request.GET['id_producto']
        cantidad = request.GET['cantidad']
        
        
        producto = Producto.objects.get(id=id_producto)

        data['id_ventaPorMenor'] = ultimo_pedido
        data['producto'] = id_producto
        data['cantidad'] = cantidad
   
        tipoMov = "Retiro Venta Por Menor"
        fecha = ultimo_pedido.fecha
        detalle = ""
        nombreProducto = producto.nombre
        
        usuario = request.user.username
        
        stock = int(producto.stock)
        
        if stock > 0 and int(cantidad) <= stock:
            print(stock)
            formulario = detalleVentaPorMenorForm(data)
            if formulario.is_valid():
                
                formulario.save()

                if id_producto:
                    
                    stockProducto = int(producto.stock) - int(cantidad)
                    producto.stock = stockProducto
                    producto.save()
                    cargarStock(ultimo_pedido.id, tipoMov, fecha, detalle, cantidad, nombreProducto, stockProducto, usuario)
                messages.add_message(request, messages.SUCCESS, "El retiro de mercaderia para venta por menor se registró exitosamente")

                return HttpResponse(True)
            messages.add_message(request, messages.ERROR, "Error en el registro de detalle")    
            return JsonResponse({"error": "Error"}, status=400)
        else:
            messages.add_message(request, messages.ERROR,  "no hay stock o no hay la cantidad deseada del producto seleccionado")
    return JsonResponse({"error": "Error"}, status=400)


def detalleRetiroVenta(request):
    
    if request.is_ajax():
        id = request.POST.get("id")
        pago = DetalleventaPorMenor.objects.filter(id_ventaPorMenor=id).values('producto__nombre','cantidad')
        
        return JsonResponse({"data": list(pago)})


def eliminarVentaMenor(request, id):
    venta = get_object_or_404(ventaPorMenor, pk=id)
    
    if venta:
        detalle = DetalleventaPorMenor.objects.filter(id_ventaPorMenor = id).values('producto', 'cantidad')
      
        for d in detalle:
            producto = Producto.objects.get(id=d['producto'])
            stockProducto = int(producto.stock) + int(d['cantidad'])
            producto.stock = stockProducto
            producto.save()
            

        venta.delete()
        eliminarStock(id, tipo="Retiro Venta Por Menor")
        messages.add_message(request, messages.SUCCESS, "Se eliminó exitosamente")
        return redirect(to='retiroVentaPorMenor')