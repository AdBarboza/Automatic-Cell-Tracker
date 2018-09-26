from django.urls import path
from components.busqueda import views as busqviews

from . import views

urlpatterns = [
    path('', busqviews.busqueda_nombre, name="busqueda_nombre")
]