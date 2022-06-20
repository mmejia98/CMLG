import re
from django.http import HttpResponse
from django.template import *
from django.shortcuts import *
from .models import Catalogo, Paquete, EspecificacionPaquete
# Estos metodos hacen referencia a las paginas creadas.
# Agrega aqui tu pagina declarando un metodo

def verPaquetes(request):
    paquetes = Paquete.objects.all().select_related('especificacionpaquete')
    catalogos = Catalogo.objects.all()
    return render(request, "catalogo.html",{
        'paquetes' : paquetes,
        'catalogos' : catalogos,
        })

def paquete1(request):
    return 0

def verEspecificacionPaquete(request, id):
    idPaquete = id
    paquete = Paquete.objects.get(id=id)
    especificacionPaquete = EspecificacionPaquete.objects.get(id__exact=paquete.especificacionpaquete_id)
    return HttpResponse(especificacionPaquete)

def verCatalogo(request, id):
    paquetes = Paquete.objects.filter(catalogo_id=id).select_related('especificacionpaquete')
    catalogos = Catalogo.all()
    return render(request, "catalogo.html",{
        'paquetes' : paquetes,
        'catalogos' : catalogos,
        })