import json
from json.encoder import JSONEncoder
from django.shortcuts import render
from django.db.models import Sum
from compras.models import detalleCompra
from django.http import HttpResponse, response
from django.http import JsonResponse
from django.db.models.functions import Extract
# Create your views here.

def index(request):
    # if request.is_ajax() and request.method == "POST":
    #     compra = detalleCompra.objects.values('id_compra__id', 'id_compra__comprobante', 'id_compra__fecha').annotate(Sum('total'))
    #     return HttpResponse(True)
    return render(request, 'cedal/index.html')

def graficoCompras(request):
    
    if request.is_ajax() and request.method == "GET":
        
        #compra = detalleCompra.objects.values('id_compra__fecha').annotate(Sum('total')).order_by(Extract('id_compra__fecha', 'month') )
        compra = detalleCompra.objects.values('id_compra__fecha__month').order_by('id_compra__fecha__month').annotate(Sum('total')) 
        #compra = detalleCompra.objects.values(month=TruncMonth('id_compra__fecha__month').order_by('id_compra__fecha').annotate(Sum('total'))
        # data = {
        #     'datos': compra
        # }
        

        return JsonResponse({"data": list(compra)})
        
    return render(request, 'cedal/index.html')
    