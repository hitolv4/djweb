from django.conf.urls import url

from . import views

urlpatterns = [

]


urlpatterns = [

    url(r'^contacto/$', views.email, name='email'),
    url(r'^success/$', views.success, name='success'),

]
