from django.contrib import admin
from .models import Cliente,Empleado,Usuario
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('usuario','servicio_Contratado','proyecto')
admin.site.register(Cliente, ClienteAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username','telefono')
admin.site.register(Usuario, UsuarioAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
admin.site.register(Empleado, EmpleadoAdmin)