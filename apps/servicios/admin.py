from django.contrib import admin
from .models import Proyecto,Festival,Estado_Proyecto,Publicidad,Galeria
# Register your models here.

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
admin.site.register(Proyecto, ProyectoAdmin)

class FestivalAdmin(admin.ModelAdmin):
    list_display = ('nombre','anyo')
admin.site.register(Festival, FestivalAdmin)

class Estado_ProyectoAdmin(admin.ModelAdmin):
    list_display = ('proyecto','festival','estado')
admin.site.register(Estado_Proyecto, Estado_ProyectoAdmin)

class PublicidadAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
admin.site.register(Publicidad, PublicidadAdmin)

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('imagen','proyecto')
admin.site.register(Galeria, GaleriaAdmin)