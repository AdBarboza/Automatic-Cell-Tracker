from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session as session
from django.http import HttpResponse
from components.parma.forms import PhotoUploadForm
from components.parma.models import ImageUpload
import requests
from io import BytesIO
from io import StringIO
from PIL import Image
import os

from .segmentation import segmentation

from time import gmtime, strftime

def detector(request):
    #ImageUpload.objects.all().delete()
    if request.method == 'POST':
      form = PhotoUploadForm(request.POST, request.FILES or None)
      if form.is_valid():
          pic = request.FILES['file']
          path = './components/parma/static/results/' + pic.name
          segmentation.segmentacion_imagen(pic.read(), path)
          img = ImageUpload(filename=pic.name, path= 'results/' + pic.name)
          img.save()
          
    images = ImageUpload.objects.all()
    return render(request, 'detector.html', {'images_processed':images})

