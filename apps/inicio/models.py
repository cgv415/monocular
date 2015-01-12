from django.db import models

# Create your models here.


class VideoInicial(models.Model):
    codigo = models.TextField()
    activo = models.BooleanField(default=True)

    