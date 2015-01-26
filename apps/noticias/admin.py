from django.contrib import admin
from .models import Noticia
# Register your models here.

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha','activo')
admin.site.register(Noticia, NoticiaAdmin)