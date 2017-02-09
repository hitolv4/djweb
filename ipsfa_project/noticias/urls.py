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

    # statico beneficios
    url(r'^beneficiarios/afiliacion/$', views.bafiliacion, name='bafiliacion'),
    url(r'^beneficiarios/afiliacion/(?P<pk>\d+)/$',
        views.detalle3, name='detalle3'),
    url(r'^beneficiarios/bienestar_y_seguridad_social/$',
        views.bbienestar, name='bbienestar'),
    url(r'^beneficiarios/beneficios_del_trabajador/$',
        views.btrabajador, name='btrabajador'),
    url(r'^beneficiarios/sisa/$', views.bsisa, name='sisa'),
    url(r'^beneficiarios/creditos/$', views.bcreditos, name='creditos'),
    url(r'^beneficiarios/inversora/$', views.binversora, name='inversora'),

    # statico institucion
    url(r'^institucion/aspectos_legales/consejo_directivo/$',
        views.consejodirectivo, name='consejodirectivo'),
    url(r'^institucion/aspectos_legales/marco_juridico/$',
        views.marcojuridico, name='marcojuridico'),
    url(r'^institucion/contrataciones_publicas', views.contratacionespublicas,
        name='contratacionespublicas'),
    url(r'^institucion/efemerides', views.efemerides, name='efemerides'),
    url(r'^institucion/organizacion/quienes_somos', views.quienessomos,
        name='quienessomos'),
    url(r'^institucion/organizacion/heraldia_del_escudo',
        views.heraldiaescudo, name='heraldiaescudo'),
    url(r'^institucion/organizacion/himno', views.himno, name='himno'),
    url(r'^institucion/organizacion/plan_de_transformacion',
        views.plant, name='plant'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
