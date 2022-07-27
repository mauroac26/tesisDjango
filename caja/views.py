from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from .forms import movCajaForm
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
        id = Caja.objects.order_by('id').last()
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
                        
                        post.saldo = monto + float(ultimo_saldo)
                    else:
                        post.saldo = float(ultimo_saldo) - monto
                
                fecha = datetime.now()
                post.fecha = fecha
                post.id_caja = id
                post.save()
        else:
            messages.add_message(request, messages.ERROR, "La caja debe abrirse antes de realizar un movimiento")
            #data["mensaje"] = ultimo_saldo
    # hoy = datetime.now()
    # caja = movCaja.objects.filter(fecha__range=[hoy - timedelta(days=1), hoy + timedelta(days=1)])
    caja = movCaja.objects.all()
    data["caja"] = caja

    return render(request, 'caja/caja.html', data)


def aperturaCaja(request):

    caja = Caja.objects.all()

    if caja:
        print(Caja.objects.latest('id').id)
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
    



