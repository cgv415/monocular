from django.db import models

# Create your models here.

#Modelo para el video inicial 
class VideoInicial(models.Model):
    codigo = models.TextField()
    activo = models.BooleanField(default=True)

    