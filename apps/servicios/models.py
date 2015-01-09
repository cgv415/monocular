from django.db import models
from apps.administracion.models import Cliente

ESTADOS = (
   ('seleccionado', 'Seleccionado'),
   ('premiado', 'Premiado'),
)
# Create your models here.
class Corto(models.Model):
    titulo=models.CharField(max_length=100)
    palmares=models.TextField()
    duracion = models.IntegerField(default='0')
    anyo=models.DateField('yyyy')
    pais=models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    reparto =models.CharField(max_length=50)
    productora =models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    sinopsis = models.TextField()
    trailer = models.CharField(max_length=100,null=True)
    imagen = models.ImageField(upload_to = 'cortometrajes')
    cliente = models.OneToOneField(Cliente)
    
    
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