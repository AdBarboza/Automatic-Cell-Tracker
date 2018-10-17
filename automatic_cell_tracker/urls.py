from django.contrib import admin
from django.contrib.auth import urls as authurls
from django.urls import path
from django.conf.urls import include, url

from django.conf import settings
from django.urls import include

urlpatterns = [
    url(r'admin/', admin.site.urls),
    path('', include('components.login.urls')),
    path('analisis/', include('components.analisis.urls')),
    path('home/', include('components.home.urls')),
    path('experimento/', include('components.experimento.urls')),
    path('busqueda/', include('components.busqueda.urls')),
    path('bitacora/', include('components.bitacora.urls')),
    path('informe/', include('components.informes.urls')),
    path('tratamientos/', include('components.tratamiento.urls')),
    path('correo/',include('components.correo.urls'))
]
