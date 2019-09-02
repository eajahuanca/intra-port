from django.urls import path
from .views import (
    api_get_tiposoporte_view,
    api_detail_tiposoporte_view,
    api_create_tiposoporte_view,
    api_update_tiposoporte_view,
    api_delete_tiposoporte_view
)

urlpatterns = [
    path('api/get', api_get_tiposoporte_view, name='get_tiposoporte'),
    path('api/<pk>/', api_detail_tiposoporte_view, name='detalle_tiposoporte'),
    path('api/create', api_create_tiposoporte_view, name='create_tiposoporte'),
    path('api/<pk>/update', api_update_tiposoporte_view, name='update_tiposoporte'),
    path('api/<pk>/delete', api_delete_tiposoporte_view, name='delete_tiposoporte')
]
