from django.urls import path
from components.busqueda import views as busqviews

from . import views

urlpatterns = [
    path('', busqviews.busqueda_home, name="busqueda_home"),
    path('paciente', busqviews.busqueda_nombre, name="busqueda_nombre"),
    path('analisis', busqviews.busqueda_analisis, name="busqueda_analisis"),
    path('tratamiento', busqviews.busqueda_tratamiento, name="busqueda_tratamiento")
]