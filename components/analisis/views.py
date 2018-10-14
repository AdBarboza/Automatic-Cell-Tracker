from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session as session
from django.http import HttpResponse
from .segmentation import segmentation
from components.analisis.forms import ResultadoForm, UploadFileForm
from components.analisis import models
import requests
from io import BytesIO
from io import StringIO
from PIL import Image
import os

from components.experimento.models import Experimento

import cloudinary

guardado = False

@login_required
def analisis(request):
    imgsrc = "https://uploads-ssl.webflow.com/57e5747bd0ac813956df4e96/5aebae14c6d254621d81f826_placeholder.png"
    form = UploadFileForm(request.POST, request.FILES)
    
    if request.method == 'POST':
        if form.is_valid():
            #do things
            imagen = form.cleaned_data['file']
            cld = cloudinary.uploader.upload(imagen)
            url = cld['url']
            request.session['url'] = url
            return render(request, 'subir.html', {'form': form, 'imgsrc' : url})


    return render(request, 'subir.html', {'form': form, 'imgsrc' : imgsrc})

# Create your views here.
@login_required
def resultados(request):
    form = ResultadoForm(request.POST, request.FILES)

    all_entries = Experimento.objects.all()
    form.fields['experimento'].choices = [ (o.id, o.nombre) for o in all_entries]

    url = request.session['url']
    url_r = ''
    if guardado:
        url_r = request.session['url_r']
    else:
        url_r = segmentation.segmentacion_imagen(url)
        request.session['url_r'] = url_r

    return render(request, 'resultados.html',{'original':url, 'resultado': url_r, 'form': form})

@login_required
def guardar_resultados(request):
    form = ResultadoForm(request.POST, request.FILES)
    if form.is_valid():
        experimento = form.cleaned_data['experimento']
        print("Experimento ID: ", experimento)
        url = request.session['url']
        url_r = request.session['url_r']
        fch_m = form.cleaned_data['Fecha_Muestra']
        fch_a = form.cleaned_data['Fecha_Analisis']
        obs = form.cleaned_data['Observaciones']

        resultado = models.Resultado(experimento = experimento, url_original = url, url_resultado = url_r,
                                        fch_muestra = fch_m, fch_analisis = fch_a, observaciones = obs)
        print("AHHHHHHHHHHHHHHHHHHHHHHHHHH")
        resultado.save()

    return redirect('resultados')

@login_required
def descargar_resultado(request):

    url_r = request.session['url_r']
    response = requests.get(url_r)
    img = Image.open(BytesIO(response.content))
    img.save(os.path.join(os.path.expanduser("~"), "Downloads" + '/resultado.png'))
    print(url_r)
    return redirect(url_r)
    
