from django.contrib import admin
from django.contrib.auth import urls as authurls
from django.urls import path
from django.conf.urls import include, url
from components.home import views as homeviews
from components.analisis import views as analisisviews
from django.conf import settings
from django.urls import include

urlpatterns = [
    url(r'admin/', admin.site.urls),
    path('', include('components.home.urls')),
    path('analisis/', homeviews.analisis, name='analisis'),
    path('index/', homeviews.index, name='index'),
    path('resultados/', analisisviews.resultados, name='resultados'),
    path('guardar_resultados/', analisisviews.guardar_resultados, name='guardar_resultados'),
    path('descargar_resultado/', analisisviews.descargar_resultado, name='descargar_resultado'),
    path('experimento/', include('components.experimento.urls')),
<<<<<<< HEAD
    path('busqueda/', include('components.busqueda.urls'))
=======
    path('busqueda/', include('components.busqueda.urls')),
    path('tratamientos/', include('components.tratamiento.urls'))
>>>>>>> tratamiento
]
