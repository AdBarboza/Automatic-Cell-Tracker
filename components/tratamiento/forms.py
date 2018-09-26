from django import forms
import datetime
from datetimepicker.widgets import DateTimePicker


# Form tratamientos
class TratamientoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=100)
    fch_inicio = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'datepicker'}))
    fch_fin = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'datepicker'}))