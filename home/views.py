from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def vista_registro(request):
    formulario = forms_registro()
    return render(request,'registro.html')


def vista_lista(request):
    return render (request,'lista.html')

def vista_registrar_cuenta(request):
    return render(request, 'registrar_cuenta.html')

def vista_cliente(request):
    return render(request, 'cliente.html')