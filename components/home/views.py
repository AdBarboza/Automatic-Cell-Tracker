from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session as session
from django.http import HttpResponse
from components.home.forms import UploadFileForm
import cloudinary
# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

# Create your views here.
@login_required
def resultados(request):
    return render(request, 'resultados.html')

    
@login_required
def analisis(request):
    imgsrc = "https://uploads-ssl.webflow.com/57e5747bd0ac813956df4e96/5aebae14c6d254621d81f826_placeholder.png"
    form = UploadFileForm(request.POST, request.FILES)
    
    if request.method == 'POST':
        if form.is_valid():
            #do things
            imagen = form.cleaned_data['file']
            print("IMAGEN: ",type(imagen))
            cld = cloudinary.uploader.upload(imagen)
            url = cld['url']
            request.session['url'] = url
            return render(request, 'subir.html', {'form': form, 'imgsrc' : url})


    return render(request, 'subir.html', {'form': form, 'imgsrc' : imgsrc})