from time import strftime
from django.db import models

# Create your models here.

class Reporte(models.Model):
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.fechaCreacion.strftime("%Y-%m-%d %H:%M:%S")