from inspect import classify_class_attrs
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from paquete.models import *
from reporte.models import *
from django.contrib.auth.models import User

# Create your models here.

class Pago(models.Model):
    tipo = models.CharField(max_length=20)
    monto = models.FloatField()
    def __str__(self):
        return str(self.monto)

class Reserva(models.Model):
    pago = models.OneToOneField(Pago, on_delete=models.CASCADE)
    catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE)
    reporte = models.ForeignKey(Reporte, null=True, blank=True, on_delete=models.SET_NULL)
    ticket = models.CharField(max_length=8, unique=True)
    pagado = models.BooleanField()
    fecha = models.DateField()
    hora = models.TimeField()
    def __str__(self):
        return self.ticket

class Reserva_User(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    