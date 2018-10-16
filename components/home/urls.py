from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from components.home import views as homeviews


urlpatterns = [
    path('', homeviews.index, name='index'),
]