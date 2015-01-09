from django.db import models

# Create your models here.
ESTADOS = (
   ('seleccionado', 'Seleccionado'),
   ('premiado', 'Premiado'),
)

class Menu(models.Model):
    titulo=models.CharField(max_length=50)
    cod = models.IntegerField()