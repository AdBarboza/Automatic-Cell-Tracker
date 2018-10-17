from django import forms

from components.experimento.models import Experimento
from components.tratamiento.models import Tratamiento


class InformeForm(forms.Form):
    experimento = forms.ModelChoiceField(queryset=Experimento.objects.all(), initial=None, required=False)
    tratamiento = forms.ModelChoiceField(queryset=Tratamiento.objects.all(), initial=None, required=False)
