from django.shortcuts import render


def lista_publicaciones(request):
    return render(request, 'noticias/lista_publicaciones.html')
