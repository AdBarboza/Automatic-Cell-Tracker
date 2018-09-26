from django.db import models

class Tratamiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    fch_inicio = models.DateTimeField()
    fch_fin = models.DateTimeField()

class ObservacionTratamiento(models.Model):
    descripcion = models.CharField(max_length=200)
    fk_tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
