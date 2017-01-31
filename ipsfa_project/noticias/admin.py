from django.contrib import admin
from .models import (Nota, UltimaHora, YoutubeSlide,
                     Slider, CarouselNota, GaleriaExpresidentes,
                     LineaDeMando, Militar, Componente, Rango, Sucursal, Gerencia, Beneficio, BeneficioDocumento)

# Register your models here.

# Admin de Notas


class ImagesInline(admin.StackedInline):
    model = CarouselNota
    extra = 3


class NotaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nueva Nota', {'fields': ['autor', 'titulo', 'texto']}),
        ('Imagenes', {'fields': ['portada']}),
        ('Fechas', {'fields': ['fecha_creacion', 'fecha_publicacion']}),
    ]
    inlines = [ImagesInline]

# Admin de Beneficio


class DocumentosInline(admin.StackedInline):
    model = BeneficioDocumento
    extra = 1
    

class BeneficioAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos', {'fields': ['autor', 'dependencia', 'beneficio', 
                              'texto', 'fecha_creacion', 'fecha_publicacion']})
    ]
    inlines = [DocumentosInline]


admin.site.register(Nota, NotaAdmin)

admin.site.register(UltimaHora)

admin.site.register(YoutubeSlide)

admin.site.register(Slider)

admin.site.register(GaleriaExpresidentes)

admin.site.register(LineaDeMando)

admin.site.register(Militar)

admin.site.register(Sucursal)

admin.site.register(Gerencia)

# habilita admin para componente y rangos
admin.site.register(Componente)

admin.site.register(Rango)

admin.site.register(Beneficio, BeneficioAdmin)
