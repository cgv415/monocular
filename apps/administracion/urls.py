from django.conf.urls import url
from .views import Registrarse, RegistrarCorto
from django.contrib.auth.views import login
#from django.contrib.auth.views import logout

urlpatterns = [
   #url(r'^$' , 'apps.inicio.views.index'),
   url(r'^admin/$' , 'apps.administracion.views.Principal',name="principal"),
   url(r'^registrarCorto/', RegistrarCorto.as_view(), name="registrar_corto"),
   url(r'^registrarse/$' , Registrarse.as_view(),name="registrarse"),
   url(r'^main$', 'apps.administracion.views.main', name='main'),
   url(r'^signup$', 'apps.administracion.views.signup', name='signup'),
   url(r'^$', login, {'template_name': 'administracion/login.html', }, name="login"),
   url(r'^home$', 'apps.administracion.views.home', name='home'),
   url(r'^logout/$' , 'django.contrib.auth.views.logout_then_login',name='logout'),

   ]