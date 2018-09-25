"""automatic_cell_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import urls as authurls
from django.urls import path
from django.conf.urls import include, url
from components.home import views as homeviews
from components.analisis import views as analisisviews
from components.tratamiento import views as tratamientoviews
from django.conf import settings

urlpatterns = [
    url(r'admin/', admin.site.urls),
    path('', include('components.home.urls')),
    path('analisis/', homeviews.analisis, name='analisis'),
    path('index/', homeviews.index, name='index'),
    path('resultados/', analisisviews.resultados, name='resultados'),
    path('guardar_resultados/', analisisviews.guardar_resultados, name='guardar_resultados'),
    path('descargar_resultado/', analisisviews.descargar_resultado, name='descargar_resultado'),
    path('tratamientos/', tratamientoviews.index_tratamiento, name='tratamientos_crud'),
    path('tratamientos/crear_tratamiento', tratamientoviews.crear_tratamiento, name='tratamientos_crear'),
    path('tratamientos/form_crear_tratamiento', tratamientoviews.form_crear_tratamiento, name="form_crear_tratamiento")

]
