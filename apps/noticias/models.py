from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

#Model Noticias
class Noticia(models.Model):
    activo = models.BooleanField(default=True)
    titulo= models.CharField(max_length=200)
    texto = RichTextField()
    #texto=models.TextField()
    resumen = models.TextField()
    imagen = models.ImageField(upload_to='noticias')
    fecha = models.DateField()
    def __unicode__(self):
        return self.titulo