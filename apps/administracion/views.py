#from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext

from apps.servicios.models import Proyecto, Festival, Estado_Corto,Publicidad
from apps.noticias.models import Noticia
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView


# Create your views here.
#Vista principal de la administracion
def Principal(request):
    return render_to_response('administracion/admin.html',context_instance=RequestContext(request))


#Operaciones sobre Proyecto
class ProyectosList(ListView):
    model = Proyecto
class RegistrarCorto(CreateView):
    template_name='administracion/registrar.html'
    model = Proyecto
    fields=['cliente','titulo','sinopsis','duracion','anyo','pais','director','reparto','productora','genero','trailer','imagen']
    success_url = '/administracion/proyectoslist'
class ModificarCorto(UpdateView):
    model = Proyecto
    fields=['cliente','titulo','sinopsis','duracion','anyo','pais','director','reparto','productora','genero','trailer','imagen']
    template_name='administracion/modificar.html'
    success_url = '/administracion/proyectoslist'    
class DeleteProyecto(DeleteView):
    template_name='administracion/delete.html'
    model = Proyecto
    success_url = '/administracion/proyectoslist'
    
#Operaciones sobre Noticias   
class NoticiasList(ListView):
    model = Noticia    
class RegistrarNoticia(CreateView):
    template_name='administracion/registrar.html'
    model = Noticia
    fields=['titulo','texto','resumen','fecha','imagen']
    success_url = '/administracion/noticiaslist'
class ModificarNoticia(UpdateView):
    model = Noticia
    fields=['titulo','resumen','texto','fecha','imagen']
    template_name='administracion/modificar.html'
    success_url = '/administracion/noticiaslist'
class DeleteNoticia(DeleteView):
    template_name='administracion/delete.html'
    model = Noticia
    success_url = '/administracion/noticiaslist'
    
#Operaciones sobre Festivales
class FestivalesList(ListView):
    model = Festival
class RegistrarFestival(CreateView):
    template_name='administracion/registrar.html'
    model = Festival
    fields=['nombre','ciudad','pais','anyo','fecha','web']
    success_url = '/administracion/festivaleslist'
class ModificarFestival(UpdateView):
    model = Festival
    fields=['nombre','ciudad','pais','anyo','fecha','web']
    template_name='administracion/modificar.html'
    success_url = '/administracion/festivaleslist'    
class DeleteFestival(DeleteView):
    template_name='administracion/delete.html'
    model = Festival
    success_url = '/administracion/festivaleslist'  
    
#Operaciones sobre Estados
class EstadosList(ListView):
    model = Estado_Corto
class RegistrarEstado(CreateView):
    template_name='administracion/registrar.html'
    model = Estado_Corto
    fields=['corto','festival','estado']
    success_url = '/administracion/estadoslist'
class ModificarEstado(UpdateView):
    model = Estado_Corto
    fields=['corto','festival','estado']
    template_name='administracion/modificar.html'
    success_url = '/administracion/estadoslist'
class DeleteEstado(DeleteView):
    template_name='administracion/delete.html'
    model = Estado_Corto
    success_url = '/administracion/estadoslist'   

#Operaciones sobre Estados
class PublicidadDetails(ListView):
    model = Publicidad

class CreateAnuncio(CreateView):
    template_name='administracion/registrar.html'
    model = Publicidad
    fields=['titulo','imagen','video']
    success_url = '/administracion/publicidadDetails'

class UpdateAnuncio(UpdateView):
    template_name='administracion/modificar.html'
    model = Publicidad
    fields=['titulo','imagen','video']
    success_url = '/administracion/publicidadDetails'

class DeleteAnuncio(DeleteView):
    template_name='administracion/delete.html'
    model = Publicidad
    fields=['titulo','imagen','video']
    success_url = '/administracion/publicidadDetails'

#Cambiar
def VerUsuarios(request):
    usuarios = User.objects.all().filter(is_staff=False)
    return render_to_response('administracion/verUsuarios.html',{'usuarios': usuarios},context_instance=RequestContext(request))

def VerAdministradores(request):
    administradores = User.objects.all().filter(is_staff=True)
    return render_to_response('administracion/verAdministradores.html',{'administradores': administradores},context_instance=RequestContext(request))