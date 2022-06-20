import re
from django.http import HttpResponse
from django.template import *
from django.shortcuts import *
from .models import Paquete, EspecificacionPaquete
# Estos metodos hacen referencia a las paginas creadas.
# Agrega aqui tu pagina declarando un metodo

def verPaquetes(request):
    #paquetes = Paquete.objects.all()
    #return HttpResponse(paquetes)
    return render(request, "catalogo.html",None)

def paquete1(request):
    return 0

def verEspecificacionPaquete(request, id):
    idPaquete = id
    paquete = Paquete.objects.get(id=id)
    especificacionPaquete = EspecificacionPaquete.objects.get(id__exact=paquete.especificacionpaquete_id)
    return HttpResponse(especificacionPaquete)

def verCatalogo(requets, id):
    paquetes = Paquete.objects.filter(catalogo_id=id)
    return HttpResponse(paquetes)



