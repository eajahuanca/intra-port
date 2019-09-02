from django.db import models
from django.utils.translation import ugettext_lazy as _
from modulos.administracion.models import LogModel
from modulos.seguridad.models import Usuario
from modulos.personal.models import Persona


class TipoSoporte(LogModel):
    """
    Clase Tipo de Soporte y Sistemas involucrados
    """
    tipo = models.CharField(_('Tipo de Soporte'), max_length=100, null=False, blank=False)
    descripcion = models.CharField(_('Descripcion del tipo de soporte'), max_length=200, null=False, blank=False)
    icono = models.CharField(_('Icono del Tipo de soporte'), max_length=20, null=False, blank=False)
    sistema = models.CharField(_('Sistema involucrado'), max_length=100, null=False, blank=False)
    sigla_sistema = models.CharField(_('Sigla del Sistema'), max_length=20, null=False, blank=False)
    activo = models.BooleanField(_('Estado del Tipo de soporte'), default=True)


class EstadoSolicitud(LogModel):
    """
    Clase Estado de la Solicitud, clasificado por colores
    """
    estado = models.CharField(_('Estado de la Solicitud'), max_length=50, null=False, blank=False)
    color = models.CharField(_('Color del estado'), max_length=10, null=False, blank=False)


class Calificacion(LogModel):
    """
    Clase Calificacion de la solucion del soporte
    """
    calificacion = models.CharField(_('Calificacion'), max_length=50, null=False, blank=False)
    color = models.CharField(_('Color'), max_length=15, null=False, blank=False)


class Solicitud(models.Model):
    """
    Clase Solcitud para realizar el soporte respectivo
    """
    solicitante = models.ForeignKey(Persona, null=False, blank=False, related_name='solicitud_persona', on_delete=models.PROTECT)
    estado = models.ForeignKey(EstadoSolicitud, null=False, blank=False, related_name='solicitud_estadosolicitud', on_delete=models.PROTECT)
    fecha_solicitud = models.DateTimeField(_('Fecha y hora de solicitud'), null=False, blank=False)
    tiposoporte = models.ForeignKey(TipoSoporte, null=False, blank=False, related_name='solicitud_tiposoporte', on_delete=models.PROTECT)
    descripcion_solicitud = models.CharField(_('Descripcion de la solicitud'), max_length=150, null=False, blank=False)
    fecha_solucion = models.DateTimeField(_('Fecha y hora de solucion'), null=False, blank=False)
    descripcion_solucion = models.CharField(_('Descripcion de la solucion'), max_length=250, null=False, blank=False)
    calificacion = models.ForeignKey(Calificacion, related_name='solicitud_calificacion', on_delete=models.PROTECT, null=False, blank=False)
    usuario_soporte = models.ForeignKey(Usuario, related_name='solicitud_usuariosoporte', on_delete=models.PROTECT, null=False, blank=False)

