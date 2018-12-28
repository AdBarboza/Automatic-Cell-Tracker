from django.db import models


class ImageUpload(models.Model):
    filename = models.CharField(max_length=500)
    path = models.CharField(max_length=500)

    objects = models.Manager()