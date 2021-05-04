from django.shortcuts import render
from django.http import HttpResponse
from django.views.defaults import page_not_found

# Create your views here.
def inicio(request):
    return render(request, template_name='CargarArchivo.html')

def info(request):
    return render(request, template_name='Info.html')

def error(request, exception):
    return page_not_found(request, template_name='404.html')