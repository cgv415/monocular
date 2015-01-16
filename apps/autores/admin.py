from django.contrib import admin
from .models import Autor,Libro
# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
admin.site.register(Autor, AutorAdmin)

class LibroAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
admin.site.register(Libro, LibroAdmin)