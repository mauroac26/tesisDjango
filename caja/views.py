from django.shortcuts import render
from .forms import cajaForm
from .models import Caja
from datetime import datetime, date, timedelta
# Create your views here.


def index(request):

    data = {
        "form": cajaForm()
    }
     
    if request.method == "POST":
        formulario = cajaForm(data=request.POST)
        if formulario.is_valid():
            #operacion = request.POST.get("operacion", "")
            operacion = formulario.cleaned_data['operacion']
            filtro = Caja.objects.all()
            post = formulario.save(commit=False)
            monto = float(formulario.cleaned_data['monto'])
            
            if not filtro:
                if operacion == 0:
                    post.saldo = monto
                else:
                    post.saldo = -monto
            else:
                ultimo_saldo = Caja.objects.latest('fecha').saldo
                if operacion == 0:
                    
                    post.saldo = monto + float(ultimo_saldo)
                else:
                    post.saldo = float(ultimo_saldo) - monto
            
            fecha = datetime.now()
            post.fecha = fecha
            post.save()
            
            #data["mensaje"] = ultimo_saldo
    hoy = datetime.now()
    caja = Caja.objects.filter(fecha__range=[hoy - timedelta(days=1), hoy + timedelta(days=1)])
    #caja = Caja.objects.all()
    data["cajaIngreso"] = caja

    return render(request, 'caja/caja.html', data)

# def ingresoDinero(request):

#     data = {
#         "form": cajaForm()
#     }

#     return render(request, 'caja/ingresoDinero.html', data)