from django.shortcuts import render


from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def index(request):
    return HttpResponse("asdf")