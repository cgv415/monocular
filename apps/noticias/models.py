from django.db import models
# Create your models here.
class Noticia(models.Model):
    titulo= models.CharField(max_length=100)
    texto=models.TextField()
    imagen = models.ImageField(upload_to='noticias')
    resumen = models.TextField()
    fecha = models.DateTimeField()