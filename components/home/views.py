from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session as session
from django.http import HttpResponse
from components.home.forms import UploadFileForm
import cloudinary

from components.experimento.models import Experimento
# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')
