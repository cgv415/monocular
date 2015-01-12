from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView,FormView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template import RequestContext

from apps.servicios.models import Corto, Festival
from apps.noticias.models import Noticia
from .forms import UserForm
from .models import Cliente
from forms import SignUpForm


# Create your views here.
def Principal(request):
    return render_to_response('administracion/admin.html',context_instance=RequestContext(request))

def main(request):
    return render_to_response('administracion/main.html', context_instance=RequestContext(request))

# Clase en desuso
class Registrarse(FormView):
    template_name='administracion/signup.html'
    form_class=UserForm
    success_url = reverse_lazy('registrarse')
    
    def form_valid(self,form):
        user = form.save()
        cliente = Cliente()
        cliente.usuario = user
        cliente.telefono = form.cleaned_data['telefono']
        cliente.servicio_Contratado = form.cleaned_data['servicio_Contratado']
        cliente.proyecto = form.cleaned_data['proyecto']
        cliente.save()
        return super(Registrarse,self).form_valid(form)

class RegistrarCorto(CreateView):
    template_name='administracion/registrar.html'
    model = Corto
    fields=['cliente','titulo','sinopsis','duracion','anyo','pais','director','reparto','productora','genero','trailer','imagen']
    success_url = reverse_lazy('administracion')

class RegistrarFestival(CreateView):
    template_name='administracion/registrar.html'
    model = Festival
    fields=['nombre','ciudad','pais','anyo','fecha','web']
    success_url = reverse_lazy('administracion')

@login_required()
def home(request):
    usuario = request.user
    if usuario.is_staff:
        return render_to_response('administracion/admin.html', {'user': request.user}, context_instance=RequestContext(request)) 
    else:
        return render_to_response('administracion/admin.html', {'user': request.user}, context_instance=RequestContext(request)) 
    
        
def signup(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
 
            # Process the data in form.cleaned_data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
 
            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
 
            # Save new user attributes
            user.save()
            
            #Creating Perfil
            cliente = Cliente()
            cliente.usuario = user
            cliente.telefono = form.cleaned_data['telefono']
            cliente.servicio_Contratado = form.cleaned_data['servicio_Contratado']
            cliente.proyecto = form.cleaned_data['proyecto']
            cliente.save()
 
            return HttpResponseRedirect(reverse('main'))  # Redirect after POST
    else:
        form = SignUpForm()
 
    data = {
        'form': form,
    }
    return render_to_response('administracion/signup.html', data, context_instance=RequestContext(request))
   
class RegistrarNoticia(CreateView):
    template_name='administracion/registrar.html'
    model = Noticia
    fields=['titulo','resumen','texto','fecha','imagen']
    success_url = reverse_lazy('noticias')
    
def VerCortos(request):
    cortos = Corto.objects.all().order_by('id').reverse()
    return render_to_response('administracion/verCortos.html',{'cortos': cortos},context_instance=RequestContext(request))

def VerNoticias(request):
    noticias = Noticia.objects.all().order_by('id').reverse()
    return render_to_response('administracion/verNoticias.html',{'noticias': noticias},context_instance=RequestContext(request))

def VerUsuarios(request):
    usuarios = User.objects.all().filter(is_staff=False)
    return render_to_response('administracion/verUsuarios.html',{'usuarios': usuarios},context_instance=RequestContext(request))

def VerAdministradores(request):
    administradores = User.objects.all().filter(is_staff=True)
    return render_to_response('administracion/verAdministradores.html',{'administradores': administradores},context_instance=RequestContext(request))

def VerFestivales(request):
    festivales = Festival.objects.all()
    return render_to_response('administracion/verFestivales.html',{'festivales': festivales},context_instance=RequestContext(request))
