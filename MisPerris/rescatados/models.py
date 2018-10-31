from django.db import models 
from django.utils import timezone

# modelo formulario
class FormularioAdopcion(models.Model):
    rut = models.CharField(max_length=12, help_text="Ej: 12.123.123-1" , unique=True)
    correo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=60, help_text="Nombre Completo")
    fechaNac = models.DateTimeField(default=timezone.now)
    region = models.CharField(max_length=60, help_text="region")
    ciudad = models.CharField(max_length=60, help_text="ciudad")
    tipoVivienda = models.CharField(max_length=60, help_text="vivienda")

#cada vez se configura algo de la tabla o BD
#python manage.py makemigrations
#pythons manage.py migrate

#guardar en git
#git commit -a -m "nombre commit"
#git push -u origin master
    
    #muestra rut en shell
    def __str__(self):
        return self.rut
    #acorta la variable
    def snippet(self):
        return self.correo[:15] + '...'

