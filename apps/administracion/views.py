from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,FormView
from django.core.urlresolvers import reverse_lazy
from apps.servicios.models import Corto
from .forms import UserForm
from .models import Cliente
from forms import SignUpForm
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse

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
    template_name='administracion/registrarCorto.html'
    model = Corto
    fields=['titulo','palmares','anyo','pais','director','reparto','productora','genero','sinopsis','imagen']
    success_url = reverse_lazy('distribucion')

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

    
