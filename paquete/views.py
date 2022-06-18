from django.http import HttpResponse
from django.template import *
from django.shortcuts import *

# Estos metodos hacen referencia a las paginas creadas.
# Agrega aqui tu pagina declarando un metodo

def paquete1(request):
    return HttpResponse('<h1 style="text-align:center;">Paquete1</h1>')


