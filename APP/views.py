from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('<h1 style="text-align:center;">Pagina inicio</h1>')

def inicio(request):
    return HttpResponse('<h1>pene</h1>')