from django.urls import path
from components.bitacora import views as bitviews

from . import views

urlpatterns = [
    path('', bitviews.bitacora_list, name='bitacora')
]