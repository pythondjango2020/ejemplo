from django.urls import path
from .views import *

urlpatterns =[
    path('',vista_registrar,name='about'),
    path('lista',vista_lista,name= 'lista'),
    path('registrar cuenta',vista_registrar_cuenta, name= 'registrar cuenta'),
    path('cliente',vista_cliente,name='cliente'),
]