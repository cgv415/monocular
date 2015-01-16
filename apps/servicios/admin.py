from django.contrib import admin
from .models import Proyecto,Festival,Estado_Corto,Servicio,Publicidad,Galeria
# Register your models here.

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
admin.site.register(Proyecto, ProyectoAdmin)

class FestivalAdmin(admin.ModelAdmin):
    list_display = ('nombre','anyo')
admin.site.register(Festival, FestivalAdmin)

class Estado_CortoAdmin(admin.ModelAdmin):
    list_display = ('corto','festival','estado')
admin.site.register(Estado_Corto, Estado_CortoAdmin)

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
admin.site.register(Servicio, ServicioAdmin)

class PublicidadAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
admin.site.register(Publicidad, PublicidadAdmin)

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
admin.site.register(Galeria, GaleriaAdmin)