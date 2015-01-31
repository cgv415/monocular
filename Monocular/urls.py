from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'Monocular.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.inicio.urls')),
    url(r'^noticias/', include('apps.noticias.urls')),
    url(r'^servicios/', include('apps.servicios.urls')),
    url(r'^administracion/', include('apps.administracion.urls')),
    url(r'^contacto/', include('apps.administracion.urls')),
    url(r'^portfolio/', include('apps.portfolio.urls')),
    
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT,}),
]
