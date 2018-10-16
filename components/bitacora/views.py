from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from components.bitacora.models import Bitacora

@login_required
def bitacora_list(request):
    all_entries = Bitacora.objects.all()
    return render(request, 'bitacora.html', {'object_list': all_entries})

