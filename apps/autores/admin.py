from django.contrib import admin
from .models import Autor
# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
admin.site.register(Autor, AutorAdmin)
