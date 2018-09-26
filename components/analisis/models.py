from django.db import models
from components.experimento.models import Experimento

# Create your models here.
class Resultado(models.Model):
    experimento = models.ForeignKey(Experimento, on_delete=models.CASCADE)
    url_original = models.CharField(max_length=100)
    url_resultado = models.CharField(max_length=100)
    fch_muestra = models.DateTimeField()
    fch_analisis = models.DateTimeField()
    observaciones = models.CharField(max_length=1000)

    objects = models.Manager()