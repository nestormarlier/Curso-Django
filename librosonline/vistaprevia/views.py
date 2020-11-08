from django.shortcuts import render

# Create your views here.

def bienvenida(request):
    data = { 'nombre_pagina': 'Libros online'}
    return render(request,'vistaprevia/index.html', data)
