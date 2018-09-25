from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session as session
from django.shortcuts import render
from django.http import HttpResponse
from components.tratamiento.forms import TratamientoForm
# Create your views here.

tratamientos = [{"id":12, "nombre":"t1","descripcion":"asd"}]
cont = 13

@login_required
def form_crear_tratamiento(request):
    form = TratamientoForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            t = {}
            t["id"] = cont
            t["nombre"] = form.cleaned_data["Nombre"]
            t["descripcion"] = form.cleaned_data["Descripcion"]
            t["Fecha_Inicio"] = form.cleaned_data["Fecha_Inicio"]
            t["Fecha_Fin"] = form.cleaned_data["Fecha_Fin"]
            tratamientos.append(t)
            return render(request, "index_tratamientos.html", {"tratamientos":tratamientos})


def index_tratamiento(request):
    return render(request, "index_tratamientos.html", {"tratamientos":tratamientos})


def crear_tratamiento(request):
    return render(request, "crear_tratamiento.html",{"form":TratamientoForm})