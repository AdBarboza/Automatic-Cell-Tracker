from django import forms


class BusquedaNombreForm(forms.Form):
    Nombre = forms.CharField(max_length=60)

class BusquedaAnalisisForm(forms.Form):
    Observaciones = forms.CharField(max_length=300)

class BusquedaTratamientoForm(forms.Form):
    Tratamiento = forms.CharField(max_length=60)

  