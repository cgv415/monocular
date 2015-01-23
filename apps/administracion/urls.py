from django.conf.urls import url
from .views import RegistrarCorto, RegistrarNoticia, RegistrarFestival, ModificarNoticia
from django.contrib.auth.views import login
from apps.administracion.views import ModificarCorto, DeleteNoticia, NoticiasList, ProyectosList,\
 FestivalesList, DeleteProyecto,EstadosList,ModificarEstado,DeleteEstado,ModificarFestival,DeleteFestival,RegistrarEstado,\
    PublicidadDetails, CreateAnuncio, DeleteAnuncio, UpdateAnuncio,ClientesList,ModificarCliente,RegistrarCliente,DeleteCliente,\
    RegistrarUsuario,RegistrarAdministrador,ModificarAdministrador,DeleteAdministrador,AdministradorList,RegistrarUsuarioEmpleado
# from django.contrib.auth.views import logout

urlpatterns = [
   # url(r'^$' , 'apps.inicio.views.index'),
   url(r'^admin/$' , 'apps.administracion.views.Principal', name="principal"),
   url(r'^registrarUsuario/', RegistrarUsuario.as_view(), name="registrar_Usuario"),
   url(r'^registrarUsuarioEmpleado/', RegistrarUsuarioEmpleado.as_view(), name="registrar_UsuarioEmpleado"),
   
   
   url(r'^$', login, {'template_name': 'administracion/login.html', }, name="login"),
   url(r'^logout/$' , 'django.contrib.auth.views.logout_then_login', name='logout'),
   
   url(r'^registrarAdministrador/', RegistrarAdministrador.as_view(), name="registrar_Administrador"),
   url(r'^administradorlist$', AdministradorList.as_view(), name='Administrador-list'),
   url(r'^modificarAdministrador/(?P<pk>\d+)/$', ModificarAdministrador.as_view(), name='modificar_Administrador'),
   url(r'^eliminarAdministrador/(?P<pk>\d+)/$', DeleteAdministrador.as_view(), name='eliminar_Administrador'),
   url(r'^empleado/(\d+)/$', 'apps.administracion.views.EmpleadoView', name="empleado"),
   
   url(r'^registrarCliente/', RegistrarCliente.as_view(), name="registrar_Cliente"),
   url(r'^registrarUsuario/', RegistrarUsuario.as_view(), name="registrar_Usuario"),
   url(r'^clienteslist$', ClientesList.as_view(), name='Cliente-list'),
   url(r'^modificarCliente/(?P<pk>\d+)/$', ModificarCliente.as_view(), name='modificar_Cliente'),
   url(r'^eliminarCliente/(?P<pk>\d+)/$', DeleteCliente.as_view(), name='eliminar_Cliente'),
   url(r'^cliente/(\d+)/$', 'apps.administracion.views.ClienteView', name="cliente"),
   
   url(r'^registrarProyecto/', RegistrarCorto.as_view(), name="registrar_corto"),
   url(r'^proyectoslist$', ProyectosList.as_view(), name='proyectos-list'),
   url(r'^modificarProyecto/(?P<pk>\d+)/$', ModificarCorto.as_view(), name='modificar_proyecto'),
   url(r'^eliminarProyecto/(?P<pk>\d+)/$', DeleteProyecto.as_view(), name='eliminar_proyecto'),
   
   url(r'^registrarFestival/', RegistrarFestival.as_view(), name="registrar_festival"),
   url(r'^festivaleslist$', FestivalesList.as_view(), name='festivales-list'),
   url(r'^modificarFestival/(?P<pk>\d+)/$', ModificarFestival.as_view(), name='modificar_festival'),
   url(r'^eliminarFestival/(?P<pk>\d+)/$', DeleteFestival.as_view(), name='eliminar_festival'),
   
   
   url(r'^registrarNoticia/', RegistrarNoticia.as_view(), name="registrar_noticia"),
   url(r'^noticiaslist$', NoticiasList.as_view(), name='noticiaslist'),
   url(r'^modificarNoticia/(?P<pk>\d+)/$', ModificarNoticia.as_view(), name='modificar_noticia'),
   url(r'^eliminarNoticia/(?P<pk>\d+)/$', DeleteNoticia.as_view(), name='eliminar_noticia'),

   url(r'^estadoslist$', EstadosList.as_view(), name='estados-list'), 
   url(r'^modificarEstado/(?P<pk>\d+)/$', ModificarEstado.as_view(), name='modificar_estado'),
   url(r'^eliminarEstado/(?P<pk>\d+)/$', DeleteEstado.as_view(), name='eliminar_estado'),
   url(r'^registrarEstado/', RegistrarEstado.as_view(), name="registrar_estado"),
   
   url(r'^publicidadDetails$', PublicidadDetails.as_view(), name='publicidad-details'), 
   url(r'^updateAnuncio/(?P<pk>\d+)/$', UpdateAnuncio.as_view(), name='update-anuncio'),
   url(r'^deleteAnuncio/(?P<pk>\d+)/$', DeleteAnuncio.as_view(), name='delete-anuncio'),
   url(r'^createAnuncio/', CreateAnuncio.as_view(), name="create-anuncio"),
   
   
   url(r'^verUsuarios/', 'apps.administracion.views.VerUsuarios', name="ver_usuarios"),
   url(r'^verAdministradores/', 'apps.administracion.views.VerAdministradores', name="ver_administradores"),
   

   ]
