from django.db import models
from django.contrib.auth.models import User
# Create your models here.
Tipo = (
   ('distribucion', 'Distribucion'),
   ('produccion', 'Produccion'),
   ('postproduccion', 'Postproduccion'),
   ('publicidad', 'Publicidad'),
)

Tipo = (
   ('inicio', 'Distribucion'),
   ('produccion', 'Produccion'),
   ('postproduccion', 'Postproduccion'),
)
class VideoInicial(models.Model):
    activo = models.BooleanField(default=True)
    tipo = models.CharField(max_length=30,choices=Tipo)
    codigo = models.TextField()
    
class Informacion(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField()
    direccion = models.CharField(max_length=150)
    cif = models.CharField(max_length=9)
    general = models.TextField(null = True,blank = True)

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre
    
class TextoDescriptivo(models.Model):
    tipo = models.CharField(max_length=50,choices=Tipo)
    texto = models.TextField()

class Usuario(User):
    ciudad = models.CharField(max_length=50,null=True, blank=True)
    telefono = models.PositiveIntegerField(null=True, blank=True)
     
class Cliente(models.Model):
    usuario = models.OneToOneField(User)
    ciudad = models.CharField(max_length=50)
    telefono = models.IntegerField()
    def __unicode__(self):
        return self.usuario.username
    
    
class Empleado(models.Model):
    usuario = models.OneToOneField(User)
    def __unicode__(self):
        return self.usuario.username
    
