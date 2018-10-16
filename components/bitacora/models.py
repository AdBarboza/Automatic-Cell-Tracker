from django.db import models


class Bitacora(models.Model):
    fecha = models.DateTimeField()
    categoria = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)

    objects = models.Manager()