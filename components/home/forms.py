from django import forms
import datetime
from datetimepicker.widgets import DateTimePicker

"""
    Clase del formulario del modulo de Estimacion
    Recibe Nombre y edad del paciente, y la imagen.
"""

class UploadFileForm(forms.Form):
    Patient_Name = forms.CharField(max_length=50)
    Patient_Age = forms.CharField(max_length=50)
    CHOICES=[('Male','Male'),
         ('Female','Female')]
    Patient_Sex = forms.ChoiceField(choices=CHOICES)

    file = forms.ImageField()


class ResultadoForm(forms.Form):
    Observaciones = forms.CharField(widget=forms.Textarea)
    CHOICES=[('Ivan Calvo','Ivan Calvo'),('Stuart Little','Stuart Little')]
    Paciente = forms.ChoiceField(choices=CHOICES)
    Fecha_Muestra = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'datepicker'}))
    Fecha_Analisis = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'datepicker'}))

class ExperimentoForm(forms.Form):
    nombre = forms.CharField()
    CHOICES_G=[('A','A'),('B','B'),('O','O')]
    grupo_sanguineo = forms.ChoiceField(choices=CHOICES_G)
    CHOICES_F=[('+','+'),('-','-')]
    factor_H = forms.ChoiceField(choices=CHOICES_F)
    alergias = forms.CharField(widget=forms.Textarea)
    padecimiento = forms.CharField(widget=forms.Textarea)


  