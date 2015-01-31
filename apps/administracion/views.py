#from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext

from django.contrib.admin.views.decorators import staff_member_required
from apps.servicios.models import Proyecto, Festival, Estado_Proyecto,Publicidad,\
    Galeria
from apps.noticias.models import Noticia
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView
from apps.administracion.models import Cliente, Empleado

# Create your views here.
#Vista principal de la administracion
@staff_member_required
def Principal(request):
    return render_to_response('administracion/admin.html',context_instance=RequestContext(request))

def ClienteView(request,offset):
    cod = int(offset)
    cliente = Cliente.objects.filter(id=cod)[0]
    proyectos = Proyecto.objects.filter(cliente_id = cod).order_by('-id')
    print 'usuario'
    print cliente.id
    print 'proyectos'
    for p in proyectos:
        print p.cliente_id
    return render_to_response('administracion/cliente.html',{'cliente':cliente,'proyectos':proyectos},context_instance=RequestContext(request))

def EmpleadoView(request,offset):
    cod = int(offset)
    empleado = Empleado.objects.filter(id=cod)[0]
    return render_to_response('administracion/empleado.html',{'empleado':empleado},context_instance=RequestContext(request))

class RegistrarUsuario(CreateView):
    template_name = 'administracion/registrar.html'
    fields=['username','password','first_name','last_name','email']
    model = User
    success_url = '/administracion/registrarCliente'

#Operaciones sobre Clientes
 
class ClientesList(ListView):
    model = Cliente
   
class RegistrarCliente(CreateView):
    template_name = 'administracion/registrarCliente.html'
    fields=['activo','usuario','ciudad','telefono']
    model = Cliente
    success_url = '/administracion/clienteslist'
     
class ModificarCliente(UpdateView):
    model = Cliente
    fields=['activo','usuario','ciudad','telefono']
    template_name='administracion/modificar.html'
    success_url = '/administracion/clienteslist'
    
class DeleteCliente(DeleteView):
    template_name='administracion/delete.html'
    model = Cliente
    success_url = '/administracion/clienteslist'

#Operaciones sobre Proyecto
class ProyectosList(ListView):
    model = Proyecto
    
class RegistrarCorto(CreateView):
    template_name='administracion/registrar.html'
    model = Proyecto
    fields=['activo','cliente','titulo','sinopsis','duracion','anyo','pais','director','reparto','productora','genero','trailer','imagen']
    success_url = '/administracion/proyectoslist'

   
class ModificarCorto(UpdateView):
    model = Proyecto
    fields=['activo','cliente','titulo','sinopsis','duracion','anyo','pais','director','reparto','productora','genero','trailer','imagen']
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
    fields=['activo','titulo','texto','resumen','fecha','imagen']
    success_url = '/administracion/noticiaslist'
    
class ModificarNoticia(UpdateView):
    model = Noticia
    fields=['activo','titulo','resumen','texto','fecha','imagen']
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
    fields=['activo','nombre','ciudad','pais','anyo','fecha','web']
    success_url = '/administracion/festivaleslist'

class ModificarFestival(UpdateView):
    template_name='administracion/modificar.html'
    model = Festival
    fields=['activo','nombre','ciudad','pais','anyo','fecha','web']
    success_url = '/administracion/festivaleslist'  
    
class DeleteFestival(DeleteView):
    template_name='administracion/delete.html'
    model = Festival
    success_url = '/administracion/festivaleslist'  
    
#Operaciones sobre Estados 
class EstadosList(ListView):
    model = Estado_Proyecto

class RegistrarEstado(CreateView):
    template_name='administracion/registrarEstado.html'
    model = Estado_Proyecto
    fields=['activo','proyecto','festival','estado']
    success_url = '/administracion/close'

class ModificarEstado(UpdateView):
    model = Estado_Proyecto
    fields=['activo','proyecto','festival','estado']
    template_name='administracion/modificar.html'
    success_url = '/administracion/close'

class DeleteEstado(DeleteView):
    template_name='administracion/delete.html'
    model = Estado_Proyecto
    success_url = '/administracion/close'   

#Operaciones sobre Estados  
class PublicidadDetails(ListView):
    model = Publicidad

class CreateAnuncio(CreateView):
    template_name='administracion/registrar.html'
    model = Publicidad
    fields=['activo','titulo','imagen','video']
    success_url = '/administracion/publicidadDetails'

class UpdateAnuncio(UpdateView):
    template_name='administracion/modificar.html'
    model = Publicidad
    fields=['activo','titulo','imagen','video']
    success_url = '/administracion/publicidadDetails'

class DeleteAnuncio(DeleteView):
    template_name='administracion/delete.html'
    model = Publicidad
    success_url = '/administracion/publicidadDetails'
    
#Gestion de galeria de imagenes de proyectos
class CrearImagen(CreateView):
    template_name='administracion/registrar.html'
    model = Galeria
    fields=['activo','proyecto','imagen']
    success_url = '/administracion/close'

class ModificarImagen(UpdateView):
    template_name='administracion/modificar.html'
    model = Galeria
    fields=['activo','proyecto','imagen']
    success_url = '/administracion/close'
    

class DeleteImagen(DeleteView):
    template_name='administracion/delete.html'
    model = Galeria
    success_url = '/administracion/close'

def Avanzado(request):
    return render_to_response('/admin/',context_instance=RequestContext(request))

def Close(request):
    return render_to_response('administracion/close.html',context_instance=RequestContext(request))