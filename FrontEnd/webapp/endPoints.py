from django.shortcuts import render
import requests
# Create your views here.
endpoint = 'http://127.0.0.1:8000/'

def Estadistica(request):
    contexto ={}
    if request.method == 'GET':
        form = (request.GET)
        if form.is_valid():
            r = requests.get(endpoint+'/Estadistica');
            data = r.json()
            print(data['data'])
            if data['data']==True:
                response = requests.get(endpoint+'Estadistica');
                contenido = response.json()
                contexto = {
                'contenido' : contenido,
                }
    return render(request, 'CargarArchivo.html', contexto)

def reset(request):
    contexto ={}
    if request.method == 'DELETE':
        form = (request.d)
        r = requests.post(endpoint+'/reset');
        print(r.status_code)
    else:
        print('F')
    return render(request, 'login.html', contexto)

def enviararchivo(request):
    contexto={'content':'', 'response':''}
    if request.method == 'POST':
        form = Entrada(request.POST, request.FILES)
        if form.is_valid():
            filename = request.FILES['file']
            ruta = filename.name
            with open(ruta, encoding = 'utf-8') as fil:
                contenido = fil.read()
            response = requests.post(endpoint+'Archivo', data=contenido)
            contexto = {
                'content':contenido,
                'response':response
            }
        else:
            print('no valido')
    return render(request, 'CargarArchivo.html', contexto)

def filtro1(request):
    contexto={'content':'', 'response':''}
    if request.method == 'POST':
        form = Entrada(request.POST, request.FILES)
        if form.is_valid():
            
            contenido = form
            response = requests.post(endpoint+'filtro1', data=contenido)
            contexto = {
                'content':contenido,
                'response':response
            }
        else:
            print('no valido')
    return render(request, 'Filtro1.html', contexto)

def filtro2(request):
    contexto={'content':'', 'response':''}
    if request.method == 'POST':
        form = Entrada(request.POST, request.FILES)
        if form.is_valid():
            contenido = form
            response = requests.post(endpoint+'filtro2', data=contenido)
            contexto = {
                'content':contenido,
                'response':response
            }
        else:
            print('no valido')
    return render(request, 'Filtro2.html', contexto)