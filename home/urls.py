from django.urls import path
from .views import *

urlpatterns =[
    path('',vista_about,name='about'),
]