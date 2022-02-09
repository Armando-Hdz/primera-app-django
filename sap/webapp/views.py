from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola mundo desde Django')

def despedirse(request):
    return HttpResponse('Despedida desde Django')

def contactar(Request):
    return HttpResponse('Telefono: 5501020304 \n Correo: correo@hotmail.com')