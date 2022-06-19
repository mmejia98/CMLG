from django.db import models

# Create your models here.

class EspecificacionPaquete(models.Model):
    precio = models.FloatField()
    descripcion = models.TextField()
    tipo = models.CharField(max_length=20)
    def __str__(self):
        return self.descripcion

class Catalogo(models.Model):
    departamento = models.CharField(max_length=50)
    def __str__(self):
        return self.departamento

class Paquete(models.Model):
    especificacionpaquete = models.ForeignKey(EspecificacionPaquete, on_delete=models.CASCADE)
    catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=8, unique=True, default=None)
    disponible = models.BooleanField()
    def __str__(self):
        return self.codigo