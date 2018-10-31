from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^formulario/',include('rescatados.urls')),
    url(r'^new/',include('rescatados.urls')),
    url(r'^about/$',views.about),
    url(r'^$',views.homepage)
]

urlpatterns += staticfiles_urlpatterns()