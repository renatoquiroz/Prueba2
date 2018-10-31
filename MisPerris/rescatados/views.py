from django.shortcuts import render
from .models import FormularioAdopcion

# Create your views here.
def formulario(request):
    FormAdopAll = FormularioAdopcion.objects.all().order_by('nombre')
    return render(request,'formularios/formulario.html', {'FormAdopAll':FormAdopAll})