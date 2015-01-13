from django.conf.urls import url
from .views import Registrarse, RegistrarCorto,RegistrarNoticia,RegistrarFestival,ModificarNoticia
from django.contrib.auth.views import login
from apps.administracion.views import ModificarCorto, DeleteNoticia,\
    NoticiasList, CortosList
#from django.contrib.auth.views import logout

urlpatterns = [
   #url(r'^$' , 'apps.inicio.views.index'),
   url(r'^admin/$' , 'apps.administracion.views.Principal',name="principal"),
   
   url(r'^registrarCorto/', RegistrarCorto.as_view(), name="registrar_corto"),
   url(r'^registrarFestival/', RegistrarFestival.as_view(), name="registrar_festival"),
   url(r'^registrarNoticia/', RegistrarNoticia.as_view(), name="registrar_noticia"),
   
   url(r'^verCortos/', 'apps.administracion.views.VerCortos', name="ver_cortos"),
   url(r'^verNoticias/', 'apps.administracion.views.VerNoticias', name="ver_noticias"),
   url(r'^verUsuarios/', 'apps.administracion.views.VerUsuarios', name="ver_usuarios"),
   url(r'^verAdministradores/', 'apps.administracion.views.VerAdministradores', name="ver_administradores"),
   url(r'^verFestivales/', 'apps.administracion.views.VerFestivales', name="ver_festivales"),
   
   url(r'^noticiaslist$', NoticiasList.as_view(), name='noticiaslist'),
   url(r'^cortoslist$', CortosList.as_view(), name='cortos-list'),
  
   url(r'^modificarNoticia/(?P<pk>\d+)/$', ModificarNoticia.as_view(), name='modificar_noticia'),
   url(r'^modificarCorto/(?P<pk>\d+)/$', ModificarCorto.as_view(), name='modificar_corto'),
   url(r'^eliminarNoticia/(?P<pk>\d+)/$', DeleteNoticia.as_view(), name='eliminar_noticia'),
   
   url(r'^registrarse/$' , Registrarse.as_view(),name="registrarse"),
   url(r'^main$', 'apps.administracion.views.main', name='main'),
   url(r'^signup$', 'apps.administracion.views.signup', name='signup'),
   url(r'^$', login, {'template_name': 'administracion/login.html', }, name="login"),
   #url(r'^home$', 'apps.administracion.views.home', name='home'),
   url(r'^logout/$' , 'django.contrib.auth.views.logout_then_login',name='logout'),

   ]