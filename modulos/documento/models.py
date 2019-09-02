from django.db import models
from django.utils.translation import ugettext_lazy as _
from modulos.administracion.models import LogModel


class MisionVision(LogModel):
    """
    Clase Para publicar la Mision y Vision de la institucion.
    """
    TIPO_CHOICES = (
        ("MISION", "MISION"),
        ("VISION", "VISION"),
    )
    mision = models.TextField(_('Mision de la Institucion'), null=False, blank=False)
    fecha_desde = models.DateField(_('Fecha desde'), null=False, blank=False)
    fecha_hasta = models.DateField(_('Fecha Hasta'), null=False, blank=False)
    activo = models.BooleanField(_('Estado de la mision'), default=True)
    tipo = models.CharField(_('Tipo'), max_length=15, null=False, blank=False, choices=TIPO_CHOICES, default='MISION')


class TipoContenido(LogModel):
    """
    Clase Tipo de Contenido
    """
    tipo = models.CharField(_('Tipo de Contenido'), max_length=50, null=False, blank=False)
    descripcion = models.CharField(_('Descripcion del tipo de contenido'), max_length=100, null=True, blank=True)
    activo = models.BooleanField(_('Estado del tipo de contenido'), default=True)


class Contenido(LogModel):
    """
    Clase Contenido de los archivos que contiene la intranet
    Comunicado, Anuncio, Resoluciones, Circulares, Reglamentos, Manuales
    """
    titulo = models.CharField(_('Titulo del contenido'), max_length=100, null=False, blank=False)
    descripcion = models.TextField(_('Descripcion del contenido'), null=False, blank=False)
    url = models.CharField(_('Url del contenido'), max_length=100, null=True, blank=True)
    archivo = models.FileField(_('Archivo del contenido'), upload_to='documentos_intranet/%Y/%m/', null=False, blank=False)
    mimetype = models.CharField(_('Mime Type del Archivo'), max_length=50, null=False, blank=False)
    tipo = models.ForeignKey(TipoContenido, related_name='contenido_tipocontenido', null=False, blank=False, on_delete=models.PROTECT)
    fecha_publicacion = models.DateField(_('Fecha de publicacion'), null=False, blank=False)
    fecha_limite = models.DateField(_('Fecha limite (corte de la publicacion)'), null=True, blank=True)

class Banner(LogModel):
    """
    Clase Banner para visualizar el slider de imagenes tanto en el portal web e intranet institucional
    """
    TIPO_BANNER_CHOICES = (
        ("BANNER", "BANNER"),
        ("MODAL", "MODAL"),
    )
    descripcion = models.CharField(_('Descripcion del Banner'), max_length=100, null=True, blank=True)
    imagen = models.FileField(_('Imagen cargada'), upload_to='documentos_banner/%Y/%m/', null=False, blank=False)
    tipo = models.CharField(_('Tipo'), max_length=10, null=False, blank=False,choices=TIPO_BANNER_CHOICES, default='BANNER')
    fecha_desde = models.DateField(_('Fecha Desde'), null=False, blank=False)
    fecha_hasta = models.DateField(_('Fecha Hasta'), null=False, blank=False)
    activo = models.BooleanField(_('Estado del Banner'), default=True)


class EnlacesSistemas(LogModel):
    """
    Clase Sistemas donde se registran los sistemas del mopsv para el soporte
    """
    TIPO_SISTEMA_CHOICES = (
        ("INTERNO", "INTERNO"),
        ("EXTERNO", "EXTERNO")
    )
    enlace = models.URLField(_('Url del Sistema'), null=False, blank=False)
    logo = models.ImageField(_('Logo del Sistema'), null=False, blank=False, upload_to='logosistemas/')
    nombre = models.CharField(_('Nombre del Sistema'), null=False, blank=False, max_length=50)
    tipo = models.CharField(_('Tipo de Enlace'), null=False, blank=False, max_length=15, choices=TIPO_SISTEMA_CHOICES, default='INTERNO')
    estado = models.BooleanField(_('Estado del enlace'), default=True)
