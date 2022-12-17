from django.shortcuts import render, redirect
from django.http import JsonResponse
from producto.models import Producto
from stock.forms import ajusteForm, stockForm
from django.http import HttpResponse
from datetime import datetime
from stock.models import ajusteStock, stock
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

# Create your views here.

@login_required
@permission_required('stock.view_stock', login_url='index')
def movimientoStock(request):

    stocks = stock.objects.all()

    data = {
        "stock": stocks
    }

    return render(request, 'stock/stock.html', data)


@login_required
@permission_required('stock.add_stock', login_url='index')
def altaAjuste(request):

    data = {
        "form": ajusteForm()
    }

    if request.method == "POST":
        
        

        #ultimo_ajuste = ajusteStock.objects.order_by('id', 'fecha').last()
        
        id_producto = request.POST['id_producto']
   
        cantidad = int(request.POST['cantidad'])
        detalle = request.POST['detalle']
        motivo = request.POST['motivo']
        
        producto = Producto.objects.get(id=id_producto)
        
        tipoMov = "Ajuste"
        fecha = datetime.now()
        
        nombreProducto = producto.nombre
        stockProducto = producto.stock
        usuario = request.user.username

        # data['fecha'] = datetime.now()
        # data['usuario'] = usuario
        # data['id_producto'] = id_producto
        # data['detalle'] = detalle
        # data['cantidad'] = cantidad
        # data['motivo'] = motivo
        
      
        formulario = ajusteForm(data=request.POST)
        
        if formulario.is_valid():
            
            ajuste = formulario.save(commit=False)
            ajuste.usuario_id = request.user.id
            
            ajuste.save()
            if id_producto:
                if motivo == 'Devolucion':
                    stock_actual = stockProducto + cantidad
                else:
                    stock_actual = stockProducto - cantidad

                producto.stock = stock_actual
                producto.save()
            
            id_tipo = ajusteStock.objects.order_by('id', 'fecha').last()
            cargarStock(id_tipo.id, tipoMov, fecha, detalle, cantidad, nombreProducto, stock_actual, usuario)
            messages.add_message(request, messages.SUCCESS, "El ajuste de stock se realizo exitosamente")
            return redirect(to='movimientoStock')
        data["form"] = ajusteForm()

    return render(request, 'stock/ajuste.html', data)

# def productoAuto(request):
   
#     if 'term' in request.GET:

#         producto = Producto.objects.filter(nombre__icontains=request.GET.get("term"))
#         nombre = list()
#         if producto:
            
#             for n in producto:
#                 if n.stock > n.stock_min:
#                     color = "badge-success"
#                 elif n.stock <= n.stock_min:
#                     color = "badge-warning"
#                 else:
#                     color = "badge-danger"
                
#                 dicProductos = {}
#                 dicProductos['id'] = n.id
#                 dicProductos['label'] = '<li style="font-size: 13px;" class="list-group-item d-flex justify-content-between align-items-center"><div class="col-sm-4">'+str(n.nombre)+'</div><span class="badge '+str(color)+' badge-pill text-white">'+str(n.stock)+'</span><span class="float-right">$'+str(n.precio_venta)+'</span></li>'
#                 dicProductos['value'] = n.nombre
#                 dicProductos['stock'] = n.stock
#                 dicProductos['precio'] = n.precio_compra
#                 nombre.append(dicProductos)
#             return JsonResponse(nombre, safe=False)
#         else:
#             dicProductos = {}
#             dicProductos['n'] = 1
#             dicProductos['label'] = '<li class="list-group-item align-items-center"><div class="col-sm-4"><span class="badge badge-pill badge-danger">Dar alta producto</span></div></li>'
#             nombre.append(dicProductos)
#             return JsonResponse(nombre, safe=False)


# def cargarAjuste(request):
   
#     # request should be ajax and method should be POST.
#     if request.is_ajax and request.method == "POST":
#         data = {}

#         usuario = request.user.username
        

    
#         data['fecha'] = datetime.now()
        
#         data['usuario'] = usuario
#         # get the form data
#         form = ajusteForm(data)
#         # save the data and after fetch the object in instance
#         if form.is_valid():
#             form.save()
#             #ultima_compra = Compras.objects.order_by('id', 'fecha').last()
#             return HttpResponse(True)
            

#     # some error occured
#     return JsonResponse({"error": "Error"}, status=400)


# def cargarAjuste(request):

#     if request.is_ajax():
#         data = {}
        

#         #ultimo_ajuste = ajusteStock.objects.order_by('id', 'fecha').last()
        
#         id_producto = request.GET['id_producto']
#         cantidad = int(request.GET['cantidad'])
#         detalle = request.GET['detalle']
#         motivo = request.GET['motivo']
        
#         producto = Producto.objects.get(id=id_producto)
        
#         tipoMov = "Ajuste"
#         fecha = datetime.now()
        
#         nombreProducto = producto.nombre
#         stockProducto = producto.stock
#         usuario = request.user.username

#         data['fecha'] = datetime.now()
#         data['usuario'] = usuario
#         data['id_producto'] = id_producto
#         data['detalle'] = detalle
#         data['cantidad'] = cantidad
#         data['motivo'] = motivo
        
        
#         formulario = ajusteForm(data)
        
#         if formulario.is_valid():
            
#             formulario.save()

#             if id_producto:
#                 if motivo == 'Devolucion':
#                     stock_actual = stockProducto + cantidad
#                 else:
#                     stock_actual = stockProducto - cantidad

#                 producto.stock = stock_actual
#                 producto.save()
                
#                 cargarStock(tipoMov, fecha, detalle, cantidad, nombreProducto, stock_actual, usuario)
#             messages.add_message(request, messages.SUCCESS, "El ajuste de stock se realizo exitosamente")

#             return HttpResponse(True)
            
        

#     return JsonResponse({"error": "Error"}, status=400)


def cargarStock(id_tipo, tipo, fecha, detalle, cantidad, producto, stock, usuario):
    
    productos = {}

    productos['id_tipo'] = id_tipo
    productos['tipoMovimiento'] = tipo
    productos['fecha'] = fecha
    productos['detalle'] = detalle
    productos['cantidad'] = cantidad
    productos['producto'] = producto
    productos['stockActual'] = stock
    productos['usuario'] = usuario

    formulario = stockForm(productos)

    if formulario.is_valid():
        formulario.save()


def eliminarStock(id_tipo, tipo):
    s = stock.objects.filter(id_tipo=id_tipo, tipoMovimiento = tipo)
    s.delete()

