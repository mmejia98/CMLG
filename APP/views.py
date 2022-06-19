from django.http import HttpResponse
from django.template import *
from django.shortcuts import *

# Estos metodos hacen referencia a las paginas creadas.
# Agrega aqui tu pagina declarando un metodo

def index(request):
    return HttpResponse('<h1 style="text-align:center;">Pagina inicio</h1>')

def inicio(request):
    return render(request,'inicio.html')
