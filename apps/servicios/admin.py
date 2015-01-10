from django.contrib import admin
from .models import Corto,Festival,Estado_Corto
# Register your models here.

class CortoAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
admin.site.register(Corto, CortoAdmin)

class FestivalAdmin(admin.ModelAdmin):
    list_display = ('nombre','anyo')
admin.site.register(Festival, FestivalAdmin)

class Estado_CortoAdmin(admin.ModelAdmin):
    list_display = ('corto','festival','estado')
admin.site.register(Estado_Corto, Estado_CortoAdmin)