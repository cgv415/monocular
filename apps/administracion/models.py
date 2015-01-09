from django.db import models
from django.contrib.auth.models import User
# Create your models here.
SERVICIO_CONTRATADO = (
   ('cortometraje', 'Cortometraje'),
   ('publicidad', 'Publicidad'),
   ('etanolaje', 'Etanolaje'),
   ('videoclip', 'Videoclip'),
   ('otro', 'Otro'),
)
class Cliente(models.Model):
    usuario = models.OneToOneField(User)
    ciudad = models.CharField(max_length=50)
    servicio_Contratado = models.CharField(max_length=50,choices=SERVICIO_CONTRATADO)
    proyecto =models.CharField(max_length=50)
    telefono = models.IntegerField()
    def __unicode__(self):
        return self.usuario.username
    
    
class Empleado(models.Model):
    usuario = models.OneToOneField(User)
    def __unicode__(self):
        return self.usuario.username