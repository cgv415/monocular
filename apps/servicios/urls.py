from django.conf.urls import url
#from .views import index, index2,inicio,RegistrarNoticia

urlpatterns = [
   #url(r'^$' , 'apps.inicio.views.index'),
   url(r'^$' , 'apps.servicios.views.Servicios',name="servicios"),
   url(r'^produccion' , 'apps.servicios.views.Produccion'),
   url(r'^postproduccion' , 'apps.servicios.views.Postproduccion'),
   url(r'^publicidad' , 'apps.servicios.views.Publicidad'),
   url(r'^distribucion' , 'apps.servicios.views.Distribucion',name="distribucion"),
   
   
   url(r'^corto/(\d+)/$', 'apps.servicios.views.Cortometraje', name="cortometraje"),
]