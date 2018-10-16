from django import forms

"""
    Clase del formulario del modulo de Estimacion
    Recibe Nombre y edad del paciente, y la imagen.
"""

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