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
    #experimento = forms.ChoiceField()
    Observaciones = forms.CharField(widget=forms.Textarea)
    Fecha_Muestra = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'datepicker'}))
    Fecha_Analisis = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'datepicker'}))

class ExperimentoForm(forms.Form):
    nombre = forms.CharField()
    CHOICES_S=[('F','Femenino'),('M','Masculino')]
    sexo = forms.ChoiceField(choices=CHOICES_S)
    CHOICES_G=[('AB','AB'),('A','A'),('B','B'),('O','O')]
    grupo_sanguineo = forms.ChoiceField(choices=CHOICES_G)
    CHOICES_F=[('+','+'),('-','-')]
    factor_H = forms.ChoiceField(choices=CHOICES_F)
    alergias = forms.CharField(widget=forms.Textarea)
    padecimiento = forms.CharField(widget=forms.Textarea)



  