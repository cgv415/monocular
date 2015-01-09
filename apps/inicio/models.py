from django.db import models

# Create your models here.


class Vimeo(models.Model):
    codigo = models.IntegerField()
    activo = models.BooleanField(default=True)

    