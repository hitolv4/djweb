from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lista_publicaciones, name='lista_publicaciones'),
    #url(r'^nota/(?P<pk>[0-9]+)/$', views.detalle, name='detalle'),
    url(r'^nota/(?P<pk>\d+)/$', views.detalle, name='detalle')
]
