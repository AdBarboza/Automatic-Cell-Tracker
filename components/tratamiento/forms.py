from django import forms
import datetime
from datetimepicker.widgets import DateTimePicker


# Form tratamientos
class TratamientoForm(forms.Form):
    Nombre = forms.CharField(max_length=50)
    Descripcion = forms.CharField(max_length=50)
    Fecha_Inicio = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'datepicker'}))
    Fecha_Fin = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'datepicker'}))