from django.db import models
from components.experimento.models import Experimento

class Tratamiento(models.Model):
    experimento = models.ForeignKey(Experimento, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    fch_inicio = models.DateTimeField()
    fch_fin = models.DateTimeField()
    objects = models.Manager()


class ObservacionTratamiento(models.Model):
    descripcion = models.CharField(max_length=200)
    fk_tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    objects = models.Manager()
