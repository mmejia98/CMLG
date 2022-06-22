import re
from django.http import HttpResponse
from django.template import *
from django.shortcuts import *
from .models import Catalogo, Paquete, EspecificacionPaquete
from django.views import View
# Estos metodos hacen referencia a las paginas creadas.
# Agrega aqui tu pagina declarando un metodo

class VerPaquetes(View):  
    def get(self, request):
        paquetes = Paquete.objects.all().select_related('especificacionpaquete')
        catalogos = Catalogo.objects.all()
        return render(request, "catalogo.html",{
            'paquetes' : paquetes,
            'catalogos' : catalogos,
            })

def paquete1(request):
    return 0
    
class VerEspecificacionPaquete(View):  
    def get(self, request, id):
        idPaquete = id
        paquete = Paquete.objects.get(id=id)
        especificacionPaquete = EspecificacionPaquete.objects.get(id__exact=paquete.especificacionpaquete_id)
        return HttpResponse(especificacionPaquete)

class VerCatalogo(View):  
    def get(self, request):
        if(request.GET.get('catalogo') == '0' or request.GET.get('catalogo') == ''):
            return redirect('paquetes')
        else:
            paquetes = Paquete.objects.filter(catalogo_id=request.GET.get('catalogo')).select_related('especificacionpaquete')
        catalogos = Catalogo.objects.all()
        return render(request, "catalogo.html",{
            'paquetes' : paquetes,
            'catalogos' : catalogos,
            })