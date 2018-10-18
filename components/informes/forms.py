from django import forms

from components.experimento.models import Experimento
from components.tratamiento.models import Tratamiento


class InformeFormTrat(forms.Form):
    tratamiento = forms.ModelChoiceField(queryset=Tratamiento.objects.all(), initial=None, required=False)

class InformeFormExp(forms.Form):
    experimento = forms.ModelChoiceField(queryset=Experimento.objects.all(), initial=None, required=False)
