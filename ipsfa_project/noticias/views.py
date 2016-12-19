from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Nota


def lista_publicaciones(request):
    posts = Nota.objects.filter(
        fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'noticias/lista_publicaciones.html', {'posts': posts})


def detalle(request, pk):
    post = get_object_or_404(Nota, pk=pk)
    return render(request, 'noticias/detalle.html', {'post': post})
