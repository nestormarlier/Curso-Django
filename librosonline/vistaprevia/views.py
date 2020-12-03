from django.shortcuts import render

# Create your views here.

def bienvenida(request):
    data = { 'nombre_pagina': 'Libros online'}
    return render(request,'vistaprevia/index.html', data)

def posicion_estatica(request):
    data = { 'nombre_pagina': 'Posición estática'}
    return render(request,'vistaprevia/posicion_static.html', data)

def posicion_absoluta(request):
    data = { 'nombre_pagina': 'Posición absoluta'}
    return render(request,'vistaprevia/posicion_absolute.html', data)

def posicion_relativa(request):
    data = { 'nombre_pagina': 'Posición relativa'}
    return render(request,'vistaprevia/posicion_relative.html', data)

def posicion_fija(request):
    data = { 'nombre_pagina': 'Posición fija'}
    return render(request,'vistaprevia/posicion_fixed.html', data)

def cajas_centradas(request):
    data = { 'nombre_pagina': 'Cajas centradas'}
    return render(request, 'vistaprevia/posicion_centrada.html', data)