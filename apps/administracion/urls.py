from django.conf.urls import url, include
from django.contrib.auth.views import login
from django.contrib import admin
from apps.administracion.views import RegistrarCliente, ClientesList

# from django.contrib.auth.views import logout

urlpatterns = [
   # url(r'^$' , 'apps.inicio.views.index'),
   url(r'^admin/$' , 'apps.administracion.views.Principal', name="principal"),
   url(r'^registrarUsuario/', 'apps.administracion.views.RegistrarUsuario', name="registrar_Usuario"),
   url(r'^registrarUsuarioEmpleado/', 'apps.administracion.views.RegistrarUsuarioEmpleado', name="registrar_UsuarioEmpleado"),
   
   
   url(r'^$', login, {'template_name': 'administracion/login.html', }, name="login"),
   url(r'^logout/$' , 'django.contrib.auth.views.logout_then_login', name='logout'),

   url(r'^registrarCliente/',RegistrarCliente.as_view(), name="registrar_Cliente"),
   url(r'^clienteslist$', ClientesList.as_view(), name='Cliente-list'),
   url(r'^modificarCliente/(?P<pk>\d+)/$','apps.administracion.views.ModificarCliente' , name='modificar_Cliente'),
   url(r'^eliminarCliente/(?P<pk>\d+)/$','apps.administracion.views.DeleteCliente', name='eliminar_Cliente'),
   url(r'^cliente/(\d+)/$', 'apps.administracion.views.ClienteView', name="cliente"),
   
   url(r'^registrarProyecto/','apps.administracion.views.RegistrarCorto', name="registrar_corto"),
   url(r'^proyectoslist$','apps.administracion.views.ProyectosList', name='proyectos-list'),
   url(r'^modificarProyecto/(?P<pk>\d+)/$','apps.administracion.views.ModificarCorto', name='modificar_proyecto'),
   url(r'^eliminarProyecto/(?P<pk>\d+)/$','apps.administracion.views.DeleteProyecto', name='eliminar_proyecto'),
   
   url(r'^registrarFestival/','apps.administracion.views.RegistrarFestival', name="registrar_festival"),
   url(r'^festivaleslist$','apps.administracion.views.FestivalesList', name='festivales-list'),
   url(r'^modificarFestival/(?P<pk>\d+)/$','apps.administracion.views.ModificarFestival', name='modificar_festival'),
   url(r'^eliminarFestival/(?P<pk>\d+)/$', 'apps.administracion.views.DeleteFestival', name='eliminar_festival'),
   
   
   url(r'^registrarNoticia/','apps.administracion.views.RegistrarNoticia', name="registrar_noticia"),
   url(r'^noticiaslist$','apps.administracion.views.NoticiasList', name='noticiaslist'),
   url(r'^modificarNoticia/(?P<pk>\d+)/$','apps.administracion.views.ModificarNoticia', name='modificar_noticia'),
   url(r'^eliminarNoticia/(?P<pk>\d+)/$','apps.administracion.views.DeleteNoticia', name='eliminar_noticia'),

   url(r'^estadoslist$','apps.administracion.views.EstadosList', name='estados-list'), 
   url(r'^modificarEstado/(?P<pk>\d+)/$','apps.administracion.views.ModificarEstado', name='modificar_estado'),
   url(r'^eliminarEstado/(?P<pk>\d+)/$','apps.administracion.views.DeleteEstado', name='eliminar_estado'),
   url(r'^registrarEstado/','apps.administracion.views.RegistrarEstado', name="registrar_estado"),
   
   url(r'^publicidadDetails$','apps.administracion.views.PublicidadDetails', name='publicidad-details'), 
   url(r'^updateAnuncio/(?P<pk>\d+)/$','apps.administracion.views.UpdateAnuncio', name='update-anuncio'),
   url(r'^deleteAnuncio/(?P<pk>\d+)/$','apps.administracion.views.DeleteAnuncio', name='delete-anuncio'),
   url(r'^createAnuncio/','apps.administracion.views.CreateAnuncio', name="create-anuncio"),
   
   url(r'^avanzado/', 'apps.administracion.views.Avanzado', name="avanzado"),
   url(r'^administracionAvanzada/', include(admin.site.urls),name="adminadvance"),
   ]
