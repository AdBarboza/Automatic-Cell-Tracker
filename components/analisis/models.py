from django.db import models

# Create your models here.
class Resultado(models.Model):
    url_original = models.CharField(max_length=100)
    url_resultado = models.CharField(max_length=100)
    fch_muestra = models.DateTimeField()
    fch_analisis = models.DateTimeField()
    observaciones = models.CharField(max_length=1000)
    paciente = models.CharField(max_length=50)