from django.conf.urls import url
from . import views
#from .views import list_adopcion, create_adopcion, update_adopcion, delete_adopcion
from .views import create_adopcion

urlpatterns = [
    url(r'^$',views.formulario),
    url(r'new', create_adopcion, name='create_adopcion'),
    #url(r'update/<int:id>/',update_adopcion , name='update_adopcion'),
    #url(r'delete/<int:id>/',delete_adopcion , name='delete_adopcion'),

]
