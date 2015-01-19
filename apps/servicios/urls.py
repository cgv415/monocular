from django.conf.urls import url
#from .views import index, index2,inicio,RegistrarNoticia

urlpatterns = [
   #url(r'^$' , 'apps.inicio.views.index'),
   url(r'^$' , 'apps.servicios.views.Servicios',name="servicios"),
   url(r'^produccion' , 'apps.servicios.views.Produccion',name="produccion"),
   url(r'^postproduccion' , 'apps.servicios.views.Postproduccion',name="postproduccion"),
   url(r'^publicidad' , 'apps.servicios.views.PublicidadPage',name="publicidad"),
   url(r'^distribucion' , 'apps.servicios.views.Distribucion',name="distribucion"),
   url(r'^mificha' , 'apps.servicios.views.MiFicha',name="mificha"),
   
   url(r'^ficha/(\d+)/$', 'apps.servicios.views.Ficha', name="ficha"),
   url(r'^anuncio/(\d+)/$', 'apps.servicios.views.Anuncio', name="anuncio"),
   url(r'^festival/(\d+)/$', 'apps.servicios.views.FestivalView', name="festival"),
]