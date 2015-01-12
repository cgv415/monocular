from django.contrib import admin
from .models import VideoInicial
# Register your models here.

class VideoInicialAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'activo')
admin.site.register(VideoInicial, VideoInicialAdmin)