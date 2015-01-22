# -*- coding: utf-8 -*-
from django.db import models
#from apps.administracion.models import Cliente
from django.contrib.auth.models import User
from apps.administracion.models import Servicio

ESTADOS = (
   ('seleccionado', 'Seleccionado'),
   ('premiado', 'Premiado'),
)

# Create your models here.
    
#Model Cortometraje
class Proyecto(models.Model):
    cliente = models.ForeignKey(User,null=True,blank=True)
    servicio = models.ManyToManyField(Servicio)
    portfolio = models.BooleanField(default=False)
    titulo=models.CharField(max_length=100)
    #Para mostrar ñ y acentos se escribe con la cadena u'texto con ñ'
    anyo=models.PositiveIntegerField(u'año',null=True,blank=True)
    duracion = models.CharField(max_length=100,null=True,blank=True)
    soporte = models.CharField(max_length=100,null=True,blank=True)
    formato = models.CharField(max_length=100,null=True,blank=True)
    director = models.CharField(max_length=100,null=True,blank=True)
    productora =models.CharField(max_length=100,null=True,blank=True)
    reparto =models.CharField(max_length=100,null=True,blank=True)
    sinopsis = models.TextField()
    pais=models.CharField(max_length=100,null=True,blank=True)
    genero = models.CharField(max_length=100,null=True,blank=True)
    trailer = models.TextField(null=True,blank=True)
    observaciones = models.TextField(null=True,blank=True)
    imagen = models.ImageField(upload_to = 'cortometrajes')
    #Por defecto se muestra el titulo del cortometraje
    def __unicode__(self):
        return self.titulo

class Galeria(models.Model):
    imagen = models.ImageField(upload_to = 'galeria')
    proyecto = models.ForeignKey(Proyecto)

    #Modelo Festivales
class Festival(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    anyo = models.PositiveIntegerField(u'año')
    fecha = models.CharField(max_length=100,null=True,blank=True)
    web = models.URLField(null=True,blank=True)
    def __unicode__(self):
        return self.nombre
    
#Modelo para los estados de los cortos
class Estado_Proyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto)
    festival = models.ForeignKey(Festival)
    estado = models.CharField(max_length=30,null=True,blank=True,choices=ESTADOS)
    def __unicode__(self):
        return self.estado
    
#Modelo Publicidad
class Publicidad(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to = 'publicidadgallery',null=True,blank=True)
    video = models.CharField(max_length=100,null=True,blank=True)
    def __unicode__(self):
        return self.titulo