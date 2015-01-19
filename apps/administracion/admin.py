from django.contrib import admin
from .models import Cliente,Empleado,Usuario,TextoDescriptivo
# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
admin.site.register(Cliente, ClienteAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username','telefono')
admin.site.register(Usuario, UsuarioAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
admin.site.register(Empleado, EmpleadoAdmin)

class TextoDescriptivoAdmin(admin.ModelAdmin):
    list_display = ('tipo','texto')
admin.site.register(TextoDescriptivo, TextoDescriptivoAdmin)
