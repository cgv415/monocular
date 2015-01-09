from django.conf.urls import patterns, include, url
from .views import ResgistrarAutor,ReportarAutor

urlpatterns = [

url(r'^registrar/', ResgistrarAutor.as_view(), name="registrar_autor"),
url(r'^reportar/$', ReportarAutor, name="reportar_autor"),

]
