from django.db import models

# Create your models here.


class Vimeo(models.Model):
    codigo = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    