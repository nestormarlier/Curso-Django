from django.urls import path
from .views import *

urlpatterns = [
    path('vistaprevia/', bienvenida, name="bienvenida"),
    path('estatica/', posicion_estatica, name="position_estatica"),
    path('absoluta/', posicion_absoluta, name="position_absoluta"),
    path('relativa/', posicion_relativa, name="position_relativa"),
]