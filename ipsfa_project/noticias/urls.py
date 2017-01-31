from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.lista_publicaciones, name='lista_publicaciones'),
    url(r'^nota/(?P<pk>\d+)/$', views.detalle, name='detalle'),
    url(r'^institucion/galeria_de_expresidentes/$',
        views.gal_expresidentes, name='gal_expresidentes'),
    url(r'^institucion/organizacion/linea_de_mando/$', views.linea_mando,
        name='linea_mando'),
    url(r'^institucion/sucursales/$', views.sucursales, name='sucursales'),
    url(r'^gerencias/atencion_al_afiliado/$', views.gerenciasAA,
        name='gerenciasAA'),
    url(r'^gerencias/filiales_y_u_negocio/$', views.gerenciasFyU,
        name='gerenciasFyU'),
    url(r'^gerencias/gerencias_internas/$', views.gerenciasGI,
        name='gerenciasGI'),            
    url(r'^gerencias/(?P<pk>\d+)/$', views.detalle2, name='detalle2'),
    url(r'^beneficiarios/afiliacion/$', views.bafiliacion, name='bafiliacion'),
    url(r'^beneficiarios/afiliacion/(?P<pk>\d+)/$', views.detalle3, name='detalle3'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
