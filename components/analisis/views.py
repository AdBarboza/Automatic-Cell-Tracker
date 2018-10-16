from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session as session
from django.http import HttpResponse
from .segmentation import segmentation
from components.analisis.forms import ResultadoForm, UploadFileForm
import requests
from io import BytesIO
from io import StringIO
from PIL import Image
import os

from components.experimento.models import Experimento
from components.bitacora.models import Bitacora
from components.analisis.models import Resultado

import cloudinary
from time import gmtime, strftime

guardado = False

# Create your views here.
@login_required
def resultados(request):
    global guardado
    form = ResultadoForm(request.POST, request.FILES)
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    url = request.session['url']
    url_r = ''
    if guardado or request.method == 'GET':
        url_r = request.session['url_r']
    else:
        url_r = segmentation.segmentacion_imagen(url)
        request.session['url_r'] = url_r
        guardado = True
        bitacora = Bitacora(fecha = time, categoria = "Imagen Analizada", descripcion = "Se ha hecho el análisis y segmentación con éxito.")
        bitacora.save()

    return render(request, 'resultados.html',{'original':url, 'resultado': url_r, 'form': form})

@login_required
def analisis(request):
    imgsrc = "https://uploads-ssl.webflow.com/57e5747bd0ac813956df4e96/5aebae14c6d254621d81f826_placeholder.png"
    form = UploadFileForm(request.POST, request.FILES)
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    if request.method == 'POST':
        if form.is_valid():
            #do things
            imagen = form.cleaned_data['file']
            cld = cloudinary.uploader.upload(imagen)
            url = cld['url']
            request.session['url'] = url
            bitacora = Bitacora(fecha = time, categoria = "Imagen Subida", descripcion = "Imagen subida a Cloudinary.")
            bitacora.save()
            return render(request, 'subir.html', {'form': form, 'imgsrc' : url})

    return render(request, 'subir.html', {'form': form, 'imgsrc' : imgsrc})

@login_required
def guardar_resultados(request):
    form = ResultadoForm(request.POST, request.FILES)
    print("AHHHHHHHHHHHHHHHHHHHHHHHHHH")
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    if form.is_valid():
        experimento = Experimento.objects.get(id=int(form.cleaned_data['experimento']))
        print("Experimento ID: ", experimento)
        url = request.session['url']
        url_r = request.session['url_r']
        fch_m = form.cleaned_data['Fecha_Muestra']
        fch_a = form.cleaned_data['Fecha_Analisis']
        obs = form.cleaned_data['Observaciones']
    else:
        print(form.errors)

    resultado = Resultado(experimento = experimento, url_original = url, url_resultado = url_r,
                                    fch_muestra = fch_m, fch_analisis = fch_a, observaciones = obs)
    resultado.save()
    bitacora = Bitacora(fecha = time, categoria = "Análisis Guardado", descripcion = "Se ha guardado la información del análisis hecho.")
    bitacora.save()

    return redirect('resultados')

@login_required
def descargar_resultado(request):
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    url_r = request.session['url_r']
    response = requests.get(url_r)
    img = Image.open(BytesIO(response.content))
    img.save(os.path.join(os.path.expanduser("~"), "Downloads" + '/resultado.png'))
    bitacora = Bitacora(fecha = time, categoria = "Imagen Descargada", descripcion = "Se ha descargado la imagen (" + url_r + ").")
    bitacora.save()
    return redirect(url_r)
    
