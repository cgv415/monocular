from django.db import models
# Create your models here.

#Model Noticias
class Noticia(models.Model):
    titulo= models.CharField(max_length=200)
    texto=models.TextField()
    imagen = models.ImageField(upload_to='noticias')
    resumen = models.TextField()
    fecha = models.DateField()
    def __unicode__(self):
        return self.titulo