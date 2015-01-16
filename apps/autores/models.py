from django.db import models

# Create your models here.
class Libro(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)
    
    def __unicode__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    libros = models.ManyToManyField(Libro)
    def __unicode__(self):
        return self.nombre