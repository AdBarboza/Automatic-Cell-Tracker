from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session as session
from django.shortcuts import render
from django.http import HttpResponse
from components.tratamiento.forms import TratamientoForm
# Create your views here.

tratamientos = [{"id":0, "Nombre":"t1","Descripcion":"asd", "FechaInicio":"12/09/2018", "FechaFin":"13/09/2018"}, 
                {"id":1, "Nombre":"t2","Descripcion":"asd", "FechaInicio":"12/09/2018", "FechaFin":"13/09/2018"}]
cont = 2

@login_required
def form_crear_tratamiento(request):
    form = TratamientoForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            t = {}
            t["id"] = cont
            t["Nombre"] = form.cleaned_data["Nombre"]
            t["Descripcion"] = form.cleaned_data["Descripcion"]
            t["Fecha_Inicio"] = form.cleaned_data["Fecha_Inicio"]
            t["Fecha_Fin"] = form.cleaned_data["Fecha_Fin"]
            tratamientos.append(t)
            return render(request, "index_tratamientos.html", {"tratamientos":tratamientos})


def index_tratamiento(request):
    return render(request, "index_tratamientos.html", {"tratamientos":tratamientos})


def crear_tratamiento(request):
    return render(request, "crear_tratamiento.html",{"form":TratamientoForm})

def modificar_tratamiento(request, id):
    a = tratamientos[id]
    a.pop("id", None)
    form = TratamientoForm(request.POST, initial = a)
    #form(initial=a)
    if request.method == "GET":
        #t = #Game.objects.get(id=1) # just an example
        #form(initial=t)
        return render(request,'modificar_tratamiento.html', {'form': form, "id":id})

def form_modificar_tratamiento(request):
    form = TratamientoForm(request.POST)
    print(form)
    if request.method == 'POST':
        if form.is_valid():
            t = {}
            t["id"] = form.cleaned_data["id"]
            t["Nombre"] = form.cleaned_data["Nombre"]
            t["Descripcion"] = form.cleaned_data["Descripcion"]
            t["Fecha_Inicio"] = form.cleaned_data["Fecha_Inicio"]
            t["Fecha_Fin"] = form.cleaned_data["Fecha_Fin"]

            tratamientos[int(form.cleaned_data["id"])] = t
            return redirect("tratamientos_index")  


def eliminar_tratamiento(request, id):
    if request.method == "GET":
        #id = request.GET["id"]
        for i in tratamientos:
            if i["id"] == id:
                tratamientos.remove(i)
                break
        #return render(request, "index_tratamientos.html", {"tratamientos":tratamientos})
        return redirect("tratamientos_index")
