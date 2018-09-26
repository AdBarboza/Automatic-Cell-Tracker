from django.urls import path
from components.tratamiento import views as tratamientoviews

urlpatterns = [
    path('', tratamientoviews.index_tratamiento, name='tratamientos_index'),
    path('crear_tratamiento', tratamientoviews.crear_tratamiento, name='tratamientos_crear'),
    path('form_crear_tratamiento', tratamientoviews.form_crear_tratamiento, name="form_crear_tratamiento"),
    path('eliminar_tratamiento/<int:id>/', tratamientoviews.eliminar_tratamiento, name="eliminar_tratamiento"),
    path('modificar_tratamiento/<int:id>/', tratamientoviews.modificar_tratamiento, name="modificar_tratamiento"),
    path('form_modificar_tratamiento', tratamientoviews.form_modificar_tratamiento, name="form_modificar_tratamiento"),
    path('ver_tratamiento/<int:id>/', tratamientoviews.ver_tratamiento, name="ver_tratamiento"),
    path('registrar_observacion_tratamiento/<int:id>/', tratamientoviews.registrar_observacion_tratamiento, name="registrar_observacion_tratamiento"),
    path('form_registrar_observacion', tratamientoviews.form_registrar_observacion, name='form_registrar_observacion')
]