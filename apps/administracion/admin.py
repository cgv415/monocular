from django.contrib import admin
from .models import Cliente,Empleado
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('usuario','servicio_Contratado','proyecto')
admin.site.register(Cliente, ClienteAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
admin.site.register(Empleado, EmpleadoAdmin)