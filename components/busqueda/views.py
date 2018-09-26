from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

from components.experimento.models import Experimento
from components.analisis.models import Resultado
from components.tratamiento.models import Tratamiento
from components.busqueda.forms import BusquedaNombreForm, BusquedaAnalisisForm, BusquedaTratamientoForm

@login_required
def busqueda_home(request):
    return render(request, 'busqueda_home.html')

@login_required
def busqueda_nombre(request):


    form = BusquedaNombreForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            searchterm = form.cleaned_data['Nombre']
            search_result = Experimento.objects.filter(nombre__contains=searchterm)
            return render(request, 'busqueda_list.html', {'object_list': search_result})

  
    return render(request, 'busqueda_form.html', {'form': form})


@login_required
def busqueda_analisis(request):


    form = BusquedaAnalisisForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            searchterm = form.cleaned_data['Observaciones']
            search_result = Resultado.objects.filter(observaciones__contains=searchterm)
            return render(request, 'busqueda_list_analisis.html', {'object_list': search_result})

  
    return render(request, 'busqueda_form_analisis.html', {'form': form})

    
    
@login_required
def busqueda_tratamiento(request):


    form = BusquedaTratamientoForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            searchterm = form.cleaned_data['Tratamiento']
            search_result = Tratamiento.objects.filter(descripcion__contains=searchterm)
            return render(request, 'busqueda_list_tratamiento.html', {'object_list': search_result})

  
    return render(request, 'busqueda_form_tratamiento.html', {'form': form})

