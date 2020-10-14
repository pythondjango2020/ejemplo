from django.urls import path
from .views import *

urlpatterns =[
    path('',vista_registro,name='about'),
    path('lista',vista_lista,name= 'lista'),
    path('registrar_cuenta',vista_registrar_cuenta, name= 'registrar_cuenta'),
    path('cliente',vista_cliente,name='cliente'),
]