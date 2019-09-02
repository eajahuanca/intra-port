import json
import datetime as dt
from .models import (TipoSoporte, EstadoSolicitud, Calificacion, Solicitud)
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializer import (
    TipoSoporteSerializer,
    EstadoSolicitudSerializer,
    CalificacionSerializer,
    SolicitudSerializer
)
from modulos.administracion.response import SuccessRestResponse, ErrorRestResponse


@api_view(['GET'])
def api_get_tiposoporte_view(request):
    try:
        tiposoporte = TipoSoporte.objects.filter(fecha_eliminacion__isnull=True).order_by('-fecha_creacion')
        serializer = TipoSoporteSerializer(tiposoporte, many=True)
        return SuccessRestResponse(
            message='',
            status=status.HTTP_202_ACCEPTED,
            data=serializer.data
        )
    except TipoSoporte.DoesNotExist:
        return ErrorRestResponse(
            message='No existe el tipo de soporte',
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
def api_detail_tiposoporte_view(request, pk):
    try:
        tiposoporte = TipoSoporte.objects.get(id=pk, fecha_eliminacion__isnull=True)
        serializer = TipoSoporteSerializer(tiposoporte)
        return SuccessRestResponse(serializer.data)
    except TipoSoporte.DoesNotExist:
        return ErrorRestResponse(
            message='No existe el tipo de soporte',
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_create_tiposoporte_view(request):
    tiposoporte = TipoSoporte()
    request.data['usuario_creacion'] = request.user.id
    request.data['fecha_creacion'] = dt.datetime.now()
    print(request.data)
    serializer = TipoSoporteSerializer(tiposoporte, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return SuccessRestResponse(
            message='Tipo de Soporte registrado correctamente',
            status=status.HTTP_200_OK,
            data=serializer.data
        )
    return ErrorRestResponse(
        message='No se puede registrar',
        status=status.HTTP_400_BAD_REQUEST,
        data=serializer.errors
    )


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def api_update_tiposoporte_view(request, pk):
    try:
        tiposoporte = TipoSoporte.objects.get(id=pk, fecha_eliminacion__isnull=True)
        request.data['fecha_modificacion'] = dt.datetime.now()
        request.data['usuario_modificacion'] = request.user.id
        serializer = TipoSoporteSerializer(tiposoporte, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return SuccessRestResponse(
                message='Tipo de soporte actualizado de manera correcta',
                status=status.HTTP_202_ACCEPTED,
                data=serializer.data
            )

    except TipoSoporte.DoesNotExist:
        return ErrorRestResponse(
            message='No existe el tipo de soporte',
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_delete_tiposoporte_view(request, pk):
    try:
        tiposoporte = TipoSoporte.objects.get(id=pk)
        tiposoporte.fecha_eliminacion=dt.datetime.now()
        tiposoporte.usuario_eliminacion_id=request.user.id
        tiposoporte.save()
        return SuccessRestResponse(
            message='Tipo de Soporte Eliminado',
            status=status.HTTP_202_ACCEPTED
        )
    except TipoSoporte.DoesNotExist:
        return ErrorRestResponse(
            message='No existe el Tipo de soporte',
            status=status.HTTP_404_NOT_FOUND
        )

