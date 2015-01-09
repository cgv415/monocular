from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import base

urlpatterns = [
   #url(r'^$' , 'apps.base.views.principal'),
   url(r'^/base$' , 'apps.base.views.base'),
]