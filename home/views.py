from django.shortcuts import render

# Create your views here.
def vista_registrar(request):
    return render(request,'registrar.html')


def vista_lista(request):
    return render (request,'lista.html')

def vista_registrar_cuenta(request):
    return render(request, 'registrar_cuenta.html')

def vista_cliente(request):
    return render(request, 'cliente.html')