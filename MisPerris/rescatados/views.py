from django.shortcuts import render, redirect
from .models import FormularioAdopcion
from .forms import AdopcionForm
#importa el modelo para realizar query y dar orden

def formulario(request):
    #asigna query djangoBD a variable
    FormAdopAll = FormularioAdopcion.objects.all().order_by('nombre')
    return render(request,'formularios/formulario.html', {'FormAdopAll':FormAdopAll})

def create_adopcion(request):
    form = FormularioAdopcion(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('formulario')    

    return render(request, 'formularios/Adopcion.html', {'form': form}) 