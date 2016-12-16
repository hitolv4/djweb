from django.shortcuts import render
from django.utils import timezone
from .models import Nota


def lista_publicaciones(request):
    posts = Nota.objects.filter(
        fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'noticias/lista_publicaciones.html', {'posts': posts})
