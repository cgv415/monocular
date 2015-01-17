from django.conf.urls import url
from .views import RegistrarCorto, RegistrarNoticia, RegistrarFestival, ModificarNoticia
from django.contrib.auth.views import login
from apps.administracion.views import ModificarCorto, DeleteNoticia, NoticiasList, ProyectosList,\
 FestivalesList, DeleteProyecto,EstadosList,ModificarEstado,DeleteEstado,ModificarFestival,DeleteFestival,RegistrarEstado
# from django.contrib.auth.views import logout

urlpatterns = [
   # url(r'^$' , 'apps.inicio.views.index'),
   url(r'^admin/$' , 'apps.administracion.views.Principal', name="principal"),
   
   url(r'^registrarProyecto/', RegistrarCorto.as_view(), name="registrar_corto"),
   url(r'^proyectoslist$', ProyectosList.as_view(), name='proyectos-list'),
   url(r'^modificarProyecto/(?P<pk>\d+)/$', ModificarCorto.as_view(), name='modificar_corto'),
   url(r'^eliminarProyecto/(?P<pk>\d+)/$', DeleteProyecto.as_view(), name='eliminar_noticia'),
   
   url(r'^registrarFestival/', RegistrarFestival.as_view(), name="registrar_festival"),
   url(r'^festivaleslist$', FestivalesList.as_view(), name='festivales-list'),
   url(r'^modificarFestival/(?P<pk>\d+)/$', ModificarFestival.as_view(), name='modificar_corto'),
   url(r'^eliminarFestival/(?P<pk>\d+)/$', DeleteFestival.as_view(), name='eliminar_festival'),
   
   
   url(r'^registrarNoticia/', RegistrarNoticia.as_view(), name="registrar_noticia"),
   url(r'^noticiaslist$', NoticiasList.as_view(), name='noticiaslist'),
   url(r'^modificarNoticia/(?P<pk>\d+)/$', ModificarNoticia.as_view(), name='modificar_noticia'),
   url(r'^eliminarNoticia/(?P<pk>\d+)/$', DeleteNoticia.as_view(), name='eliminar_noticia'),

   url(r'^estadoslist$', EstadosList.as_view(), name='estados-list'), 
   url(r'^modificarEstado/(?P<pk>\d+)/$', ModificarEstado.as_view(), name='modificar_estado'),
   url(r'^eliminarEstado/(?P<pk>\d+)/$', DeleteEstado.as_view(), name='eliminar_estado'),
   
   url(r'^registrarEstado/', RegistrarEstado.as_view(), name="registrar_estado"),
   url(r'^verUsuarios/', 'apps.administracion.views.VerUsuarios', name="ver_usuarios"),
   url(r'^verAdministradores/', 'apps.administracion.views.VerAdministradores', name="ver_administradores"),
   
   url(r'^$', login, {'template_name': 'administracion/login.html', }, name="login"),
   url(r'^logout/$' , 'django.contrib.auth.views.logout_then_login', name='logout'),

   ]
