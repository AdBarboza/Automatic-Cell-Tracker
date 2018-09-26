from django.urls import path
from components.experimento import views as expviews

from . import views

urlpatterns = [
    path('', expviews.ExperimentoList, name='Experimento_list'),
    path('new', expviews.ExperimentoCreate, name='Experimento_new'),
    path('view/<int:id>/', expviews.ExperimentoView, name='Experimento_view'),
    path('edit/<int:id>/', expviews.ExperimentoUpdate, name='Experimento_edit'),
    path('delete/<int:id>/', expviews.ExperimentoDelete, name='Experimento_delete'),
]