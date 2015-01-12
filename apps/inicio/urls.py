from django.conf.urls import url
from .views import index2
from django.views.generic import TemplateView

urlpatterns = [
   #url(r'^$' , 'apps.inicio.views.index'),
   url(r'^$' , 'apps.inicio.views.index'),
   url(r'^inicio' , 'apps.inicio.views.inicio'),
   url(r'^contacto' , 'apps.inicio.views.contacto',name="contacto"),
   url(r'^index/$' , index2.as_view(),name="inicio"),
   url(r'^about/', TemplateView.as_view(template_name="inicio/index02.html")),
   ]