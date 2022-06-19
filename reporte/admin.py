from django.contrib import admin
from reporte.models import Reporte

# Register your models here.

class ReporteAdmin(admin.ModelAdmin):
    list_display = ("id", "fechaCreacion")

admin.site.register(Reporte, ReporteAdmin)
