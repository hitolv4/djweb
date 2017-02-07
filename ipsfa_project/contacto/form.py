from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    cedula = forms.IntegerField(required=True)
    telefono = forms.IntegerField(required=False)
    correo = forms.EmailField(max_length=30, required=True)
    asunto = forms.CharField(max_length=70, required=True)
    mensaje = forms.CharField(widget=forms.Textarea, required=True)

