from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .form import ContactoForm

# Create your views here.


def email(request):
    if request.method == 'GET':
        form = ContactoForm()
    else:
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            cedula = form.cleaned_data['cedula']
            telefono = form.cleaned_data['telefono']
            asunto = form.cleaned_data['asunto']
            correo = form.cleaned_data['correo']
            mensaje = form.cleaned_data['mensaje']

            recipient = ['admin@example.com']
            try:
                send_mail(asunto, mensaje,
                          correo, recipient)
            except BadHeaderError:
                return httpResponse('Invalid Header Found.')
            return redirect('success')
    return render(request, 'contacto/email.html', {'form': form})


def success(request):
    return render(request, 'contacto/success.html')
