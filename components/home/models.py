from django.db import models
from cloudinary.models import CloudinaryField
from components.experimento.models import Experimento

# Create your models here.


class Image(models.Model):
    url = models.CharField(max_length=255)
