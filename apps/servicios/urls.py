from django.conf.urls import url
#from .views import index, index2,inicio,RegistrarNoticia

urlpatterns = [
   #url(r'^$' , 'apps.inicio.views.index'),
   url(r'^$' , 'apps.servicios.views.Servicios',name="servicios"),
   url(r'^produccion' , 'apps.servicios.views.Produccion',name="produccion"),
   url(r'^postproduccion' , 'apps.servicios.views.Postproduccion',name="postproduccion"),
   url(r'^publicidad' , 'apps.servicios.views.Publicidad',name="publicidad"),
   url(r'^distribucion' , 'apps.servicios.views.Distribucion',name="distribucion"),
   url(r'^mificha' , 'apps.servicios.views.MiFicha',name="mificha"),
   
   url(r'^corto/(\d+)/$', 'apps.servicios.views.Cortometraje', name="cortometraje"),
]