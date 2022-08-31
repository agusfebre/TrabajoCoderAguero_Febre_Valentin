from django.urls import path
from .views import *

urlpatterns = [
    path ('', inicio, name="inicio"),
    path('cargaProducto/', cargaProducto, name='cargaProducto'),
    path('cargaProveedor/', cargaProveedor, name='cargaProveedor'),
    path('cargaCliente/', cargaCliente, name='cargaCliente'),
]