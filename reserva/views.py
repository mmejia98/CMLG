from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def registrarse(request):
    return render(request, 'reserva/registro.html', None)    

def Crear(request):
    return render(request, 'reserva/crear.html', None)

