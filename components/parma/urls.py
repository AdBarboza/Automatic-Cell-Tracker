from django.conf.urls import url, include
from django.urls import path
from components.parma import views as parmaviews


urlpatterns = [
    path('detector', parmaviews.detector, name='detector')
]