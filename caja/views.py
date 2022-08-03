from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import cajaForm, movCajaForm, selectCaja
from .models import Caja, movCaja
from datetime import datetime, date, timedelta
from django.contrib import messages
# Create your views here.

@login_required
@permission_required('caja.add_caja', login_url='index')
def index(request):

    data = {
        "form": movCajaForm()
    }
     
    if request.method == "POST":
        id = Caja.objects.order_by('id', 'total').last()
        if id:
            formulario = movCajaForm(data=request.POST)
            if formulario.is_valid():
                #operacion = request.POST.get("operacion", "")
                operacion = formulario.cleaned_data['operacion']
                filtro = movCaja.objects.all()
                post = formulario.save(commit=False)
                monto = float(formulario.cleaned_data['monto'])
                
                
                if not filtro:
                    if operacion == 0:
                        post.saldo = monto
                    else:
                        post.saldo = -monto
                else:
                    ultimo_saldo = movCaja.objects.latest('fecha').saldo
                    
                    if operacion == 0:
                        
                        saldo = monto + float(ultimo_saldo)
                    else:
                        saldo = float(ultimo_saldo) - monto
                post.saldo = saldo
                fecha = datetime.now()
                post.fecha = fecha
                post.id_caja = id
                post.save()
                id.total = saldo
                id.save()
        else:
            messages.add_message(request, messages.ERROR, "La caja debe abrirse antes de realizar un movimiento")
            #data["mensaje"] = ultimo_saldo
    # hoy = datetime.now()
    # caja = movCaja.objects.filter(fecha__range=[hoy - timedelta(days=1), hoy + timedelta(days=1)])
    caja = movCaja.objects.filter(id_caja__estado=True)
    data["caja"] = caja

    return render(request, 'caja/caja.html', data)


def aperturaCaja(request):

    caja = Caja.objects.all()

    if caja:
        id = Caja.objects.order_by('id', 'total', 'estado').last()
        
        if id.estado:
           messages.add_message(request, messages.ERROR, "La caja ya se encuentra abierta")
           return redirect(to='caja')
        else:
            caja = Caja(nombre='Caja2',total=id.total, estado=True)
            caja.save()
            id = Caja.objects.order_by('id').last()
            hoy = datetime.now()
            movimiento = movCaja(fecha=hoy, descripcion='Apertura de caja', operacion=0, monto=0, saldo = id.total, id_caja=id)
            movimiento.save()
            messages.add_message(request, messages.SUCCESS, "La caja se abrio correctamente")
            return redirect(to='caja')

    else:
        caja = Caja(nombre='Caja1',total=0)
        caja.save()
        id = Caja.objects.order_by('id').last()
        hoy = datetime.now()
        movimiento = movCaja(fecha=hoy, descripcion='Apertura de caja', operacion=0, monto=0, saldo = 0, id_caja=id)
        movimiento.save()
        messages.add_message(request, messages.SUCCESS, "La caja se abrio correctamente")
        return redirect(to='caja')
    # caja = movCaja.objects.all()
    # data["caja"] = caja

    # return render(request, 'caja/caja.html', data)


def cierreCaja(request):
    id = Caja.objects.order_by('id', 'total', 'estado').last()
    if id:
        id.estado = False
        id.save()
        hoy = datetime.now()
        movimiento = movCaja(fecha=hoy, descripcion='Cierre de caja', operacion=0, monto=0, saldo = id.total, id_caja=id)
        movimiento.save()
        messages.add_message(request, messages.SUCCESS, "La caja se cerro correctamente")
        return redirect(to='caja')
    else:
        messages.add_message(request, messages.ERROR, "No se encuentra abierta la caja")
        return redirect(to='caja')



def consultaCaja(request):
    
    data = {
        "form": selectCaja()
    }
    # data={}
    if request.method == "POST":
    # if request.is_ajax():
        
        # id = request.POST['id']
        id = request.POST.get('id_caja')

        caja = movCaja.objects.filter(id_caja=id)
        first = movCaja.objects.filter(id_caja=id).first()
        last = movCaja.objects.filter(id_caja=id).last()
        data['caja']= caja
        data['first'] = first.fecha
        data['last'] = last.fecha
        data['id'] = id
        # return JsonResponse({"data": list(caja)})

    return render(request, 'caja/consultaCaja.html', data)


def movimientoCaja(request):
    if 'term' in request.GET:
    
        caja = Caja.objects.filter(nombre__icontains=request.GET.get("term")).values('id', 'nombre')
        
       
        nombre = list()
        if caja:
            for c in caja:
                id = c['id']
                mov = movCaja.objects.filter(id_caja=id).latest('fecha')
                dicCompras = {}
                dicCompras['id'] = c['id']
                dicCompras['label'] = '<li style="font-size: 11px;" class="list-group-item d-flex justify-content-between align-items-center"><div class="col-sm-5">'+str(c['nombre'])+'</div><span>'+str(mov.fecha)+'</span></li>'
                dicCompras['value'] = f'{c["nombre"]} / {mov.fecha}'
                
                
                nombre.append(dicCompras)
            return JsonResponse(nombre, safe=False)
        else:
            dicCompras = {}
            dicCompras['n'] = 1
            dicCompras['label'] = '<li style="font-size: 11px;" class="list-group-item align-items-center"><div class="col-sm-7"><span>No se moviemientos</span></div></li>'
            nombre.append(dicCompras)
            return JsonResponse(nombre, safe=False)



