from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

from components.experimento.models import Experimento
from components.busqueda.forms import BusquedaForm
@login_required
def busqueda_nombre(request):


    form = BusquedaForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            searchterm = form.cleaned_data['Nombre']
            search_result = Experimento.objects.filter(nombre__contains=searchterm)
            return render(request, 'busqueda_list.html', {'object_list': search_result})

  
    return render(request, 'busqueda_form.html', {'form': form})

    
@login_required
def busqueda_tratamiento(request):


    form = BusquedaForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            searchterm = form.cleaned_data['Nombre']
            search_result = Experimento.objects.filter(nombre__contains=searchterm)
            return render(request, 'busqueda_list.html', {'object_list': search_result})

  
    return render(request, 'busqueda_form.html', {'form': form})



@login_required
def busqueda_analisis(request):


    form = BusquedaForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            searchterm = form.cleaned_data['Nombre']
            search_result = Resultado.objects.filter(nombre__contains=searchterm)
            return render(request, 'busqueda_list.html', {'object_list': search_result})

  
    return render(request, 'busqueda_form.html', {'form': form})