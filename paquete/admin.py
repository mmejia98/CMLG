from django.contrib import admin
from paquete.models import Paquete, EspecificacionPaquete, Catalogo

# Register your models here.

class PaqueteAdmin(admin.ModelAdmin):
    list_display = ("id", "especificacionpaquete", "catalogo", "codigo", "disponible")

class EspecificacionPaqueteAdmin(admin.ModelAdmin):
    list_display = ("id", "precio", "descripcion", "tipo")

class CatalogoAdmin(admin.ModelAdmin):
    list_display = ("id", "departamento")

admin.site.register(Paquete, PaqueteAdmin)
admin.site.register(EspecificacionPaquete,  EspecificacionPaqueteAdmin)
admin.site.register(Catalogo, CatalogoAdmin)
