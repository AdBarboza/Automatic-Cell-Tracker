from django import forms
import datetime
from datetimepicker.widgets import DateTimePicker

"""
    Clase del formulario del modulo de Estimacion
    Recibe Nombre y edad del paciente, y la imagen.
"""

class UploadFileForm(forms.Form):
    file = forms.ImageField()


class ResultadoForm(forms.Form):
    experimento = forms.ChoiceField()
    Observaciones = forms.CharField(widget=forms.Textarea)
    Fecha_Muestra = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'datepicker'}))
    Fecha_Analisis = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'datepicker'}))