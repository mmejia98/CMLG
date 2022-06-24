from select import select
from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    dui = models.CharField(max_length=10, default='None')
    nit = models.CharField(max_length=14, default='None')
    permiso_residencia = models.CharField(max_length=10, default='None')
    pasaporte = models.CharField(max_length=10, default='None')
    sexo = models.CharField(max_length=20)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    pais_residencia = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre + " " +self.apellido