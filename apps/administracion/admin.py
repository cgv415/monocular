from django.contrib import admin
from .models import Cliente,Empleado,Servicio,TextoDescriptivo,VideoInicial,Informacion
# Register your models here.

class InformacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email','cif')
admin.site.register(Informacion, InformacionAdmin)

class VideoInicialAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'activo')
admin.site.register(VideoInicial, VideoInicialAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
admin.site.register(Cliente, ClienteAdmin)

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
admin.site.register(Servicio, ServicioAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
admin.site.register(Empleado, EmpleadoAdmin)

class TextoDescriptivoAdmin(admin.ModelAdmin):
    list_display = ('tipo','texto')
admin.site.register(TextoDescriptivo, TextoDescriptivoAdmin)
