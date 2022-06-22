from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class RegistrarPersona(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    def get(self, request):
        return render(request, 'reserva/registro.html', None)    
    def post(self, request):
        pass

class CrearReserva(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    def get(self, request):
        return render(request, 'reserva/crear.html', None)
    def post(self, request):
        pass

