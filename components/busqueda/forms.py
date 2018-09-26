from django import forms


class BusquedaForm(forms.Form):
    Nombre = forms.CharField(max_length=60)

  