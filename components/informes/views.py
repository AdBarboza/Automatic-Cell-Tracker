from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session as session
from django.http import HttpResponse
from components.informes.forms import InformeFormTrat, InformeFormExp
import requests
from io import BytesIO
from io import StringIO
from PIL import Image
import os

from components.experimento.models import Experimento
from components.bitacora.models import Bitacora
from components.analisis.models import Resultado
from components.tratamiento.models import Tratamiento, ObservacionTratamiento

import cloudinary
from time import gmtime, strftime

# time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
# bitacora = Bitacora(fecha = time, categoria = "Imagen Analizada", descripcion = "Se ha hecho el análisis y segmentación con éxito.")
# bitacora.save()


@login_required
def informe(request):
    formexp = InformeFormExp(request.POST, request.FILES)
    formtrat = InformeFormTrat(request.POST, request.FILES)

    return render(request,'informe.html',{'form_exp': formexp,'form_trat': formtrat})


@login_required
def informe_experimento(request):
  form = InformeFormExp(request.POST, request.FILES)
  if form.is_valid() and (request.method == 'POST'):
    experimento = form.cleaned_data['experimento']
    print("ME CAGO EN TODO!: "+ str(experimento.id))
    list_analisis = []
    list_tratamientos = []
    if experimento is not None:
      list_analisis = Resultado.objects.all().filter(experimento=experimento)
      list_tratamientos = Tratamiento.objects.all().filter(experimento=experimento)
    return render(request, 'informe_exp.html',{'Experimento': experimento, 'list_analisis': list_analisis, 'list_tratamientos': list_tratamientos})


@login_required
def informe_tratamiento(request):
  form = InformeFormTrat(request.POST, request.FILES)
  if form.is_valid() and request.method == 'POST':
    tratamiento = form.cleaned_data['tratamiento']
    print("ME CAGO EN TODO!: "+ str(tratamiento.id))
    list_experimentos = []
    list_observaciones = []
    if tratamiento is not None:
      list_experimentos = [tratamiento.experimento]
      list_observaciones = ObservacionTratamiento.objects.all().filter(fk_tratamiento=tratamiento)
      print("ME CAGO EN TODO!: "+ str(tratamiento.id))
    return render(request, 'informe_trat.html',{'Tratamiento': tratamiento, 'list_experimentos': list_experimentos, 'list_observaciones': list_observaciones, 'EXP':tratamiento.experimento})

