from django import forms
from .models import FormularioAdopcion

class AdopcionForm(forms.ModelForm):
    class Meta:
        model = FormularioAdopcion
        fields = ['rut', 'correo', 'nombre', 'fechaNac', 'region', 'ciudad', 'tipoVivienda']