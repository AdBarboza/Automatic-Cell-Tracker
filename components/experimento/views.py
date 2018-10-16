from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from components.experimento.forms import ExperimentoForm

from components.experimento.models import Experimento
from components.bitacora.models import Bitacora
from time import gmtime, strftime

@login_required
def ExperimentoList(request):
    all_entries = Experimento.objects.all()
    return render(request, 'experimento_list.html', {'object_list': all_entries})

@login_required
def ExperimentoView(request,id):
    obj = Experimento.objects.get(id=id)
    return render(request, 'experimento_detail.html',{'object': obj})

@login_required
def ExperimentoCreate(request):
    form = ExperimentoForm(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid():
            time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            nombre = form.cleaned_data['nombre']
            sexo = form.cleaned_data['sexo']
            gp_sanguineo = form.cleaned_data['grupo_sanguineo']
            factor_h = form.cleaned_data['factor_H']
            alergias = form.cleaned_data['alergias']
            padecimiento = form.cleaned_data['padecimiento']

            resultado = Experimento(nombre = nombre, sexo = sexo, gp_sanguineo = gp_sanguineo, factor_h = factor_h,
                                         alergias = alergias, padecimiento = padecimiento)

            bitacora = Bitacora(fecha = time, categoria = "Experimento Registrado", descripcion = "Se ha registrado el experimento '" + nombre + "'.")
            bitacora.save()

            resultado.save()
            return redirect('Experimento_list')

    return render(request, 'experimento_form_create.html', {'form': form})

@login_required
def ExperimentoUpdate(request,id):
    obj = Experimento.objects.get(id=id)

    if request.method == 'POST':
        time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        form = ExperimentoForm(request.POST, request.FILES)
        if form.is_valid():
            obj.nombre = form.cleaned_data['nombre']
            obj.gp_sanguineo = form.cleaned_data['grupo_sanguineo']
            obj.factor_h = form.cleaned_data['factor_H']
            obj.alergias = form.cleaned_data['alergias']
            obj.padecimiento = form.cleaned_data['padecimiento']

            obj.save()
            bitacora = Bitacora(fecha = time, categoria = "Experimento Modificado", descripcion = "Se ha modificado el experimento '" + obj.nombre + "'.")
            bitacora.save()
            return redirect('Experimento_list')

    form = ExperimentoForm(request.POST, request.FILES)
    form.fields['nombre'].initial = obj.nombre
    form.fields['sexo'].initial = obj.sexo
    form.fields['grupo_sanguineo'].initial = obj.gp_sanguineo
    form.fields['factor_H'].initial = obj.factor_h
    form.fields['alergias'].initial = obj.alergias
    form.fields['padecimiento'].initial = obj.padecimiento

    return render(request, 'experimento_form_update.html', {'form': form, 'id':id})

@login_required
def ExperimentoDelete(request, id):
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    obj = Experimento.objects.get(id=id)
    bitacora = Bitacora(fecha = time, categoria = "Experimento Eliminado", descripcion = "Se ha eliminado el experimento '" + obj.nombre + "'.")
    bitacora.save()
    obj.delete()
    return redirect('Experimento_list')