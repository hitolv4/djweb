
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import (Nota, UltimaHora, YoutubeSlide, Slider, CarouselNota,
                     GaleriaExpresidentes, LineaDeMando, Sucursal, Gerencia, Beneficio)


def lista_publicaciones(request):
    # Noticias
    posts = Nota.objects.filter(
        fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    # Ultima Hora
    uhs = UltimaHora.objects.filter(
        fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    # Youtube Slider
    slides = YoutubeSlide.objects.filter(
        fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    # Slider
    imagenes = Slider.objects.filter(
        fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'noticias/lista_publicaciones.html', {'posts': posts, 'uhs': uhs, 'slides': slides, 'imagenes': imagenes})


def detalle(request, pk):
    post = get_object_or_404(Nota, pk=pk)
    notaimgs = CarouselNota.objects.filter(
        fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'noticias/detalle.html', {'post': post, 'notaimgs': notaimgs})


def gal_expresidentes(request):
    expre = GaleriaExpresidentes.objects.filter(
        fecha_publicacion__lte=timezone.now()).order_by('inicio')
    return render(request, 'noticias/gal_expresidentes.html', {'expre': expre})


def linea_mando(request):
    linmando = LineaDeMando.objects.filter(
        fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'noticias/linea_mando.html', {'linmando': linmando})


def sucursales(request):
    sucur = Sucursal.objects.filter(
        fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion').select_related()
    return render(request, 'noticias/sucursales.html', {'sucur': sucur})


def gerenciasAA(request):
    AA = Gerencia.objects.filter(
        fecha_publicacion__lte=timezone.now(), tipo__contains='AA').order_by('fecha_publicacion').select_related()
    return render(request, 'noticias/gerenciasAA.html', {'AA': AA})


def gerenciasFyU(request):
    FU = Gerencia.objects.filter(
        fecha_publicacion__lte=timezone.now(), tipo__contains='FyU').order_by('fecha_publicacion').select_related()
    return render(request, 'noticias/gerenciasFU.html', {'FU': FU})


def gerenciasGI(request):
    GI = Gerencia.objects.filter(
        fecha_publicacion__lte=timezone.now(), tipo__contains='GI').order_by('fecha_publicacion').select_related()
    return render(request, 'noticias/gerenciasGI.html', {'GI': GI})


def detalle2(request, pk):
    gere = get_object_or_404(Gerencia, pk=pk)
    return render(request, 'noticias/detalle2.html', {'gere': gere})


def bafiliacion(request):
    afi = Beneficio.objects.filter(
        fecha_publicacion__lte=timezone.now())

    return render(request, 'noticias/beneafiliacion.html', {'afi': afi})


def detalle3(request, pk):
    bene = get_object_or_404(Beneficio, pk=pk)
    return render(request, 'noticias/detalle3.html', {'bene': bene})


def bbienestar(request):
    return render(request, 'noticias/benebienestar.html')


def btrabajador(request):
    return render(request, 'noticias/btrabajador.html')


def bcreditos(request):
    return render(request, 'noticias/bcreditos.html')


def bsisa(request):
    return render(request, 'noticias/bsisa.html')


def binversora(request):
    return render(request, 'noticias/binversora.html')



