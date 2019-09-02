from django.db import models
from django.utils.translation import ugettext_lazy as _
from modulos.administracion.models import LogModel


class Persona(LogModel):
    """
    Clase Persona con su respectivo cargo, ip y interno asignado
    """
    ci=models.CharField(_('Nro. de documento'), max_length=15, primary_key=True)
    expedido=models.CharField(_('Expedido de CI'), max_length=15, null=False, blank=False)
    nombres=models.CharField(_('Nombre Completo'), max_length=50, null=False, blank=False)
    apellido_paterno=models.CharField(_('Apellido Paterno'), max_length=50, null=False, blank=False)
    apellido_materno=models.CharField(_('Apellido Materno'), max_length=50, null=True, blank=True)
    cargo=models.CharField(_('Cargo actual'), max_length=100, null=False, blank=False)
    area=models.CharField(_('Area organizacional actual'), max_length=100, null=False, blank=False)
    nroip=models.CharField(_('Ip asignado'), max_length=15, null=False, blank=False, unique=True)
    nrointerno=models.IntegerField(_('Nro. interno asignado'), default=0, null=False, blank=False)
