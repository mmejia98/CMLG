from django.contrib import admin

from usuario.models import Persona

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "apellido", "nacionalidad", "fecha_nacimiento", "dui", "nit", "permiso_residencia", "pasaporte", "sexo", "email", "telefono", "pais_residencia")

admin.site.register(Persona, PersonaAdmin)