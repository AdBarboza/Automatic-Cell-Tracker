from django.db import models
from django.urls import reverse


class Experimento(models.Model):
    nombre = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    gp_sanguineo = models.CharField(max_length=1)
    factor_h = models.CharField(max_length=1)
    alergias = models.CharField(max_length=1000)
    padecimiento = models.CharField(max_length=1000)

    objects = models.Manager()

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('experimento_edit', kwargs={'pk': self.pk})