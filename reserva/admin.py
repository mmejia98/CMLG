import site
from django.contrib import admin

from reserva.models import Pago, Reserva, Reserva_User

# Register your models here.

class PagoAdmin(admin.ModelAdmin):
    list_display = ("id", "tipo", "monto")

class ReservaAdmin(admin.ModelAdmin):
    list_display = ("id", "pago", "paquete", "reporte", "ticket", "pagado", "fecha", "hora")

class Reserva_UserAdmin(admin.ModelAdmin):
    list_display = ("id", "reserva", "user")

admin.site.register(Pago, PagoAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Reserva_User, Reserva_UserAdmin)