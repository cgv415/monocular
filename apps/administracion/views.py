#from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext

from apps.servicios.models import Proyecto, Festival
from apps.noticias.models import Noticia
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView


# Create your views here.
#Vista principal de la administracion
def Principal(request):
    return render_to_response('administracion/admin.html',context_instance=RequestContext(request))


#Comienzan las vistas para crear objetos con create view
class RegistrarCorto(CreateView):
    template_name='administracion/registrar.html'
    model = Proyecto
    fields=['cliente','titulo','sinopsis','duracion','anyo','pais','director','reparto','productora','genero','trailer','imagen']
    success_url = '/administracion/proyectoslist'
   
class RegistrarNoticia(CreateView):
    template_name='administracion/registrar.html'
    model = Noticia
    fields=['titulo','texto','resumen','fecha','imagen']
    success_url = '/administracion/noticiaslist'

class RegistrarFestival(CreateView):
    template_name='administracion/registrar.html'
    model = Festival
    fields=['nombre','ciudad','pais','anyo','fecha','web']
    success_url = '/administracion/verFestivales'

#Comienzan las vistas para modificar objetos con update view
class ModificarNoticia(UpdateView):
    model = Noticia
    fields=['titulo','resumen','texto','fecha','imagen']
    template_name='administracion/modificar.html'
    success_url = '/administracion/noticiaslist'
    
class ModificarCorto(UpdateView):
    model = Proyecto
    fields=['cliente','titulo','sinopsis','duracion','anyo','pais','director','reparto','productora','genero','trailer','imagen']
    template_name='administracion/modificar.html'
    success_url = '/administracion/proyectoslist'
    
#Vista de los objetos con listview
class NoticiasList(ListView):
    model = Noticia

class ProyectosList(ListView):
    model = Proyecto

#Cambiar
def VerUsuarios(request):
    usuarios = User.objects.all().filter(is_staff=False)
    return render_to_response('administracion/verUsuarios.html',{'usuarios': usuarios},context_instance=RequestContext(request))

def VerAdministradores(request):
    administradores = User.objects.all().filter(is_staff=True)
    return render_to_response('administracion/verAdministradores.html',{'administradores': administradores},context_instance=RequestContext(request))

def VerFestivales(request):
    festivales = Festival.objects.all()
    return render_to_response('administracion/verFestivales.html',{'festivales': festivales},context_instance=RequestContext(request))


#Comienzan las vistas para eliminar objetos de la base de datos con delete view
class DeleteNoticia(DeleteView):
    model = Noticia
    success_url = '/administracion/noticiaslist'
    
class DeleteProyecto(DeleteView):
    template_name='administracion/delete.html'
    model = Proyecto
    success_url = '/administracion/proyectoslist'