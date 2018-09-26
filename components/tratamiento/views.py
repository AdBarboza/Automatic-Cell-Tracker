from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session as session
from django.shortcuts import render
from django.http import HttpResponse
from components.tratamiento.forms import TratamientoForm
from components.tratamiento.models import Tratamiento
from components.tratamiento.models import ObservacionTratamiento


#tratamientos = [{"id":0, "Nombre":"t1","Descripcion":"asd", "FechaInicio":"12/09/2018", "FechaFin":"13/09/2018"}, 
#                {"id":1, "Nombre":"t2","Descripcion":"asd", "FechaInicio":"12/09/2018", "FechaFin":"13/09/2018"}]
#cont = 2

@login_required
def form_crear_tratamiento(request):
    form = TratamientoForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            descripcion = form.cleaned_data["descripcion"]
            fch_inicio = form.cleaned_data["fch_inicio"]
            fch_fin = form.cleaned_data["fch_fin"]
            
            tratamiento = Tratamiento(nombre = nombre, descripcion = descripcion, fch_inicio = fch_inicio, fch_fin = fch_fin)
            tratamiento.save()
    return redirect("tratamientos_index")



def index_tratamiento(request):
    tratamientos = Tratamiento.objects.all()
    print(tratamientos)
    return render(request, "index_tratamientos.html", {"tratamientos":tratamientos})


def crear_tratamiento(request):
    return render(request, "crear_tratamiento.html",{"form":TratamientoForm})

def modificar_tratamiento(request, id):
    t = Tratamiento.objects.get(id=id)
    form = TratamientoForm(request.POST, initial = t)
    if request.method == "GET":
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
        t = Tratamiento.objects.get(id=id)
        t.delete()
        return redirect("tratamientos_index")

def ver_tratamiento(request, id):
    t = Tratamiento.objects.get(id=id)
    obs = ObservacionTratamiento.objects.filter(fk_tratamiento=id)
    return render(request, "ver_tratamiento.html", {"tratamiento":t, "observaciones":obs})

def registrar_observacion_tratamiento(request, id):
    #registrar_observacion_tratamiento
    return render(request, "registrar_observacion.html", {"id":id})
    #pass

def form_registrar_observacion(request):
    if request.method == "POST":
        descripcion = request.POST.get("descripcion")
        fk_tratamiento = Tratamiento.objects.get(id = request.POST.get("id"))
        obs = ObservacionTratamiento(descripcion = descripcion, fk_tratamiento = fk_tratamiento)
        obs.save()
    return redirect("ver_tratamiento", id = request.POST.get("id"))
