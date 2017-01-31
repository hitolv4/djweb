from django.db import models
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey
from django.core.validators import RegexValidator
from tinymce import HTMLField

# Create your models here.


# Modelos para Pagina Principal


class Nota (models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=250, unique=True)
    texto = models.TextField()
    portada = models.ImageField(upload_to='notas', blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo


class CarouselNota (models.Model):
    autor = models.ForeignKey('auth.User')
    nota = models.ForeignKey(Nota, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='carouselnota',)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)


class UltimaHora (models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=250)
    archivo = models.FileField(upload_to='ultimahora/files', blank=True)
    imagen = models.ImageField(upload_to='ultimahora/images', blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Ultima Hora'
        verbose_name_plural = 'Ultima Hora'


class YoutubeSlide (models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=250)
    url = models.URLField()
    imagen = models.ImageField(upload_to='sliderengine')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Youtube Slider'
        verbose_name_plural = 'Youtube Slider'


class Slider (models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='slider')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider'


class GaleriaExpresidentes (models.Model):
    autor = models.ForeignKey('auth.User')
    nombre = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='galeria_expresidentes')
    inicio = models.DateField(blank=True, null=True)
    fin = models.DateField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Galeria de Expresidentes'
        verbose_name_plural = 'Galeria de Expresidentes'


class LineaDeMando (models.Model):
    autor = models.ForeignKey('auth.User')
    nombre = models.CharField(max_length=250, unique=True)
    cargo = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='linea_mando', blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.cargo

    class Meta:
        verbose_name = 'Linea de Mando'
        verbose_name_plural = 'Linea de Mando'


class Componente(models.Model):

    Aviacion = 'AV.'
    Ejercito = 'EJ.'
    GuardiaNacional = 'GN.'
    Armada = 'AR.'
    OP_COMPONENTE = (
        (Aviacion, 'Aviacion'),
        (Ejercito, 'Ejercito'),
        (GuardiaNacional, 'Guardia Nacional'),
        (Armada, 'Armada'),
    )
    componente = models.CharField(
        max_length=3,
        choices=OP_COMPONENTE,)

    def __str__(self):
        return self.componente


class Rango(models.Model):
    OP_RANGO = (
        ('G/F.', 'General en Jefe'),
        ('G/D.', 'General de Divicion'),
        ('G/B.', 'General de Brigada'),
        ('CNEL.', 'Coronel'),
        ('TCNEL.', 'Teniente Coronel'),
        ('MY.', 'Mayor'),
        ('CAP.', 'Capitan'),
        ('TTE.', 'Teniente'),
        ('AL.', 'Almirante'),
        ('V/A.', 'Vicealmirante'),
        ('C/A.', 'Contralmirante'),
        ('C/N.', 'Capitan de Navio'),
        ('C/F.', 'Capitan de Fragata'),
        ('C/C.', 'Capitan de Corbeta'),
        ('T/N.', 'Teniente de Navio'),
        ('T/F.', 'Teniente de Fragata'),

    )

    componente = models.ForeignKey(Componente)
    rango = models.CharField(
        max_length=6,
        choices=OP_RANGO
    )

    def __str__(self):
        return self.rango


class Militar (models.Model):

    autor = models.ForeignKey('auth.User')
    nombre = models.CharField(max_length=250)
    componente = models.ForeignKey(Componente)
    rango = ChainedForeignKey(
        Rango,
        chained_field="componente",
        chained_model_field="componente",
        show_all=False,
        auto_choose=True,
        sort=True,

    )
    imagen = models.ImageField(upload_to='militares')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Oficial'
        verbose_name_plural = 'Oficial'


class Sucursal (models.Model):

    OP_CIUDAD = (
        ('Caracas', 'Caracas'),
        ('Apure', 'Apure'),
        ('Barcelona', 'Barcelona'),
        ('Barinas', 'Barinas'),
        ('Barquisimento', 'Barquisimento'),
        ('Carupano', 'Carupano'),
        ('Ciudad Bolivar', 'Ciudad Bolivar'),
        ('Maracaibo', 'Maracaibo'),
        ('Maracay', 'Maracay'),
        ('Margarita', 'Margarita'),
        ('Maturin', 'Maturin'),
        ('Puerto Ayacucho', 'Puerto Ayacucho'),
        ('Punto Fijo', 'Punto Fijo'),
        ('San Cristobal', 'San Cristobal'),
        ('San Juan de los Morros', 'San Juan de los Morros'),
        ('Tucupita', 'Tucupita'),
    )
    autor = models.ForeignKey('auth.User')
    ciudad = models.CharField(
        max_length=60,
        choices=OP_CIUDAD
    )
    director = models.ForeignKey(Militar)
    correo = models.EmailField(max_length=250)
    phone_regrex = RegexValidator(
        regex=r'^(\d{4})-(\d{3}).(\d{2}).(\d{2})', message="El Formato para ingresar el numero de teledono es xxxx-xxx.xx.xx Ejemplo 0212-855.23.30")
    telefono = models.CharField(
        validators=[phone_regrex], blank=True, max_length=16)
    direccion = models.CharField(max_length=250)
    horario = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.ciudad

    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'


class Gerencia(models.Model):
    autor = models.ForeignKey('auth.User')
    gerencia = models.CharField(max_length=250)
    OP_TIPO = (
        ('AA', 'Atencion al Afiliado'),
        ('FyU', 'Filiales y Unidades de Negocio'),
        ('GI', 'Gerencias Internas'),
    )
    tipo = models.CharField(
        max_length=3,
        choices=OP_TIPO,
        default='AA'
    )
    gerente = models.ForeignKey(Militar)
    correo = models.EmailField(max_length=250)
    phone_regrex = RegexValidator(
        regex=r'^(\d{4})-(\d{3}).(\d{2}).(\d{2})', message="El Formato para ingresar el numero de teledono es xxxx-xxx.xx.xx Ejemplo 0212-855.23.30")
    telefono = models.CharField(
        validators=[phone_regrex], blank=True, max_length=16)
    direccion = models.CharField(max_length=250)
    horario = models.CharField(max_length=250)
    texto = HTMLField('Texto')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.gerencia

    class Meta:
        verbose_name = 'Gerencia'
        verbose_name_plural = 'Gerencias'


class Beneficio(models.Model):

    autor = models.ForeignKey('auth.User')

    OP_DEP = (
        ('Afiliacion', 'Afiliacion'),
        ('Bienestar y Seguridad Social', 'Bienestar y Seguridad Social'),
        ('Beneficios del Trabajador', 'Beneficios del Trabajador'),
        ('Créditos', 'Créditos'),
        ('SISA', 'SISA'),
        ('Inversora', 'Inversora'),
    )
    dependencia = models.CharField(
        max_length=100,
        choices=OP_DEP,
        default='AA'
    )
    beneficio = models.CharField(max_length=100, unique=True)
    texto = HTMLField('Texto')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.dependencia



class BeneficioDocumento(models.Model):
    autor = models.ForeignKey('auth.User')
    beneficio = models.ForeignKey(Beneficio, on_delete=models.CASCADE)
    documento = models.FileField(upload_to='beneficios', blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documento'