from django.conf.urls import url, include
from django.urls import path
from components.pdfgenerator import views as pdfviews


urlpatterns = [
    path('<int:id>/', pdfviews.generate, name='pdfgenerator'),
]