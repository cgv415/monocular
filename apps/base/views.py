from django.shortcuts import render
from .models import Menu
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView,ListView
# Create your views here.
def base(request):
    menus = Menu.objects.all()
    return render_to_response('base.html',{'menus':menus},context_instance=RequestContext(request))

def principal(request):
   menus = Menu.objects.all()
   return render_to_response('base/principal.html',{'menus':menus},context_instance=RequestContext(request))
