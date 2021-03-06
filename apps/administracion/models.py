# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
Tipo = (
    ('inicio', 'Inicio'),
    ('distribucion', 'Distribucion'),
    ('produccion', 'Produccion'),
    ('postproduccion', 'Postproduccion'),
    ('publicidad', 'Publicidad'),
)
class VideoInicial(models.Model):
    activo = models.BooleanField(default=True)
    tipo = models.CharField(max_length=30,choices=Tipo)
    codigo = models.TextField()
    
class Informacion(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField(u'teléfono')
    email = models.EmailField()
    direccion = models.CharField(u'ubicación',max_length=150)
    cif = models.CharField(max_length=9)
    general = models.TextField(null = True,blank = True)

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre
    
class TextoDescriptivo(models.Model):
    tipo = models.CharField(max_length=50,choices=Tipo)
    texto = models.TextField()

class Cliente(models.Model):
    activo = models.BooleanField(default=True)
    usuario = models.OneToOneField(User)
    ciudad = models.CharField(max_length=50)
    telefono = models.IntegerField()
    def __unicode__(self):
        return self.usuario.username
    
    
class Empleado(models.Model):
    activo = models.BooleanField(default=True)
    usuario = models.OneToOneField(User)
    def __unicode__(self):
        return self.usuario.username
    
