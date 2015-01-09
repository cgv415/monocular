from django.db import models
from apps.administracion.models import Cliente

ESTADOS = (
   ('seleccionado', 'Seleccionado'),
   ('premiado', 'Premiado'),
)
# Create your models here.
class Corto(models.Model):
    cliente = models.OneToOneField(Cliente)
    titulo=models.CharField(max_length=100)
    sinopsis = models.TextField()
    duracion = models.CharField(max_length=50)
    anyo=models.DateField()
    pais=models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    reparto =models.CharField(max_length=50)
    productora =models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    trailer = models.CharField(max_length=150,null=True)
    imagen = models.ImageField(upload_to = 'cortometrajes')
    
    
    
class Festival(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    anyo = models.PositiveIntegerField()
    fecha = models.CharField(max_length=100,null=True,blank=True)
    web = models.URLField(null=True,blank=True)
    
class Estado_Corto(models.Model):
    festival = models.OneToOneField(Festival)
    corto = models.OneToOneField(Corto)
    estado = models.CharField(max_length=30,null=True,blank=True,choices=ESTADOS)