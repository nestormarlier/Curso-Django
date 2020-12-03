from django.urls import path
from .views import *

urlpatterns = [
    path('vistaprevia/', bienvenida, name="bienvenida"),
    path('estatica/', posicion_estatica, name="position_estatica"),
    path('absoluta/', posicion_absoluta, name="position_absoluta"),
    path('relativa/', posicion_relativa, name="position_relativa"),
    path('fija/',posicion_fija, name="position_fija"),
    path('centrada/', cajas_centradas, name="position_centrada"),
    path('flotarIzquierda/', flotar_izquierda, name="float_izquierda"),
]