from django.shortcuts import render
from django.http import HttpResponse
from django.views.defaults import page_not_found

# Create your views here.
def Inicio(request):
    return render(request, template_name='Inicio.html')

def Info(request):
    return render(request, template_name='Info.html')

def Ayuda(request):
    return render(request, template_name='Ayuda.html')

def CargarArchivo(request):
    return render(request, template_name='CargarArchivo.html')

def ConsultarDatos(request):
    return render(request, template_name='ConsultarDatos.html')

def Documentacion(request):
    return render(request, template_name='Documentacion.html')

def Filtro1(request):
    return render(request, template_name='Filtro1.html')

def Filtro2(request):
    return render(request, template_name='Filtro2.html')


def error(request, exception):
    return page_not_found(request, template_name='404.html')