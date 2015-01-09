from django.contrib import admin
from .models import Vimeo
# Register your models here.

class VimeoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'activo')
admin.site.register(Vimeo, VimeoAdmin)