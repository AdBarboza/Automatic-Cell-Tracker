from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session as session
from django.http import HttpResponse
import cloudinary

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')
