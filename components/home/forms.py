from django import forms

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
  