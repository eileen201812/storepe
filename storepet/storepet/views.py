from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render 
import requests

def index(request):
    
    api_url = "https://mindicador.cl/api"
    response = requests.get(api_url)
    print('status_code -> {0}'.format(response.status_code))
    json_request = response.json()
    print('json_request -> {0}'.format(json_request))
    dolar = json_request['dolar']['valor']
    fecha = json_request['dolar']['fecha']
    print('Retornar pagina index.html')
    return render(request, 'index.html', {'dolar': dolar, 'fecha': fecha})


def galeria(request):
    print('Retornar pagina galeria.html')
    return render(request, 'galeria.html')

def servicio(request):
    print('Retornar pagina servicio.html')
    return render(request, 'servicio.html')

def registro(request):
    print('Retornar pagina registro.html')
    return render(request, 'registro.html')

def contacto(request):
    print('Retornar pagina contacto.html')
    return render(request, 'contacto.html')

