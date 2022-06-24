from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from usuario.models import Persona
from paquete.models import Paquete
from .models import Pago, Reserva, Reserva_User
from django.db import transaction

class RegistrarPersona(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    def get(self, request):
        return render(request, 'reserva/registro.html', {
            'paquete_id': request.GET.get('paquete_id')
        })    
    def post(self, request):
        paquete_seleccionado = Paquete.objects.get(id=request.POST.get('paquete_id'))
        nombre=request.POST.get('nombre')
        apellido=request.POST.get('apellido')
        nacionalidad=request.POST.get('nacionalidad')
        fecha_nacimiento=request.POST.get('fecha_nacimiento')
        dui=request.POST.get('dui')          
        sexo=request.POST.get('sexo')
        email=request.POST.get('email')
        telefono=request.POST.get('telefono')
        pais_residencia=request.POST.get('pais_residencia')
        return render(request, 'reserva/crear.html', {
            'paquete': paquete_seleccionado,
            'nombre': nombre,
            'apellido': apellido,
            'nacionalidad': nacionalidad,
            'fecha_nacimiento': fecha_nacimiento,
            'dui': dui,
            'sexo': sexo,
            'email': email,
            'telefono': telefono,
            'pais_residencia': pais_residencia,
        })

class CrearReserva(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    def post(self, request):
        paquete_id=request.POST.get('paquete_id')
        with transaction.atomic():
            try:         
                persona = Persona.objects.create(
                    nombre=request.POST.get('nombre'),
                    apellido=request.POST.get('apellido'),
                    nacionalidad=request.POST.get('nacionalidad'),
                    fecha_nacimiento=request.POST.get('fecha_nacimiento'),
                    dui=request.POST.get('dui'),          
                    sexo=request.POST.get('sexo'),
                    email=request.POST.get('email'),
                    telefono=request.POST.get('telefono'),
                    pais_residencia=request.POST.get('pais_residencia'),
                    )
                pago = Pago.objects.create(
                    tipo=request.POST.get('tipo'),
                    monto=request.POST.get('monto'),
                    )
                ticket=str(pago.id) + str(request.POST.get('paquete_id'))  + 'P' + str(persona.id) + 'QT'
                reserva = Reserva.objects.create(
                        ticket=ticket,
                        pagado=True,
                        fecha=request.POST.get('fecha'),
                        hora=request.POST.get('hora'),
                        pago_id=pago.id,
                        paquete_id=paquete_id,
                        persona_id=persona.id,
                        )
                reserva_user = Reserva_User.objects.create(
                    reserva_id = reserva.id,
                    user_id = request.user.id,
                )
                return render(request, 'inicio.html', {'mensaje_exito':'Tu reserva se a guardado con exito'})
            except Exception as e:
                mensaje_error = 'Ocurrio un error en la reserva: ' + str(e)
                return render(request, 'reserva/registro.html', {
                    'paquete_id': paquete_id,
                    'mensaje_error': mensaje_error,
                })


