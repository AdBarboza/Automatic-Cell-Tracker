from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from components.informes import views as informeviews


urlpatterns = [
    path('', informeviews.informe, name='informe')
]