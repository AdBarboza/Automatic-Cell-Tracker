from django.contrib import admin
from django.urls import path
from django.contrib.auth import urls as authurls
from django.conf.urls import include, url

from django.conf import settings
from django.urls import include

from components.correo import views as correo_views

urlpatterns = [
    path('', correo_views.index_correo, name='index_correo'),
    path('enviar_correo', correo_views.enviar_correo, name='enviar_correo')
]