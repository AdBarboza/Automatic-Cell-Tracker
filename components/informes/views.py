from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session as session
from django.http import HttpResponse
from components.informes.forms import InformeForm
import requests
from io import BytesIO
from io import StringIO
from PIL import Image
import os

from components.experimento.models import Experimento
from components.bitacora.models import Bitacora
from components.analisis.models import Resultado
from components.tratamiento.models import Tratamiento

import cloudinary
from time import gmtime, strftime

# time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
# bitacora = Bitacora(fecha = time, categoria = "Imagen Analizada", descripcion = "Se ha hecho el análisis y segmentación con éxito.")
# bitacora.save()


@login_required
def informe(request):
    form = InformeForm(request.POST, request.FILES)

    if form.is_valid() and request.method == 'POST':
      experimento = form.cleaned_data['experimento']
      tratamiento = form.cleaned_data['tratamiento']
      object_list = []
      if experimento is not None:
        object_list = Resultado.objects.all().filter(experimento=experimento)

      return render(request, 'informe_exp.html',{'Experimento': experimento, 'object_list': object_list})

    return render(request, 'informe.html',{'form': form})


@login_required
def informe_experimento(request):
    form = InformeForm(request.POST, request.FILES)

    return render(request, 'informe.html',{'form': form})
