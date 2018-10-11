from django.urls import path
from components.analisis import views as analisisviews

from . import views

urlpatterns = [
    path('', analisisviews.analisis, name='analisis'),
    path('resultados/', analisisviews.resultados, name='resultados'),
    path('guardar_resultados/', analisisviews.guardar_resultados, name='guardar_resultados'),
    path('descargar_resultado/', analisisviews.descargar_resultado, name='descargar_resultado')
]