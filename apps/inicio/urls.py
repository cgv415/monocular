from django.conf.urls import url

urlpatterns = [
   #url(r'^$' , 'apps.inicio.views.index'),
   url(r'^$' , 'apps.inicio.views.inicio',name="inicio"),
   url(r'^inicio' , 'apps.inicio.views.inicio'),
   url(r'^contacto' , 'apps.inicio.views.contacto',name="contacto"),
   url(r'^light' , 'apps.inicio.views.light',name="light"),
   ]