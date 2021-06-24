from django.urls import path,include
from . import views

urlpatterns = [
    
    #lista de video juegos
    path('listar_videojuegos', views.listar_videojuegos, name = "listar_videojuegos"),

    #agregar videojuego
    path('agregar_videojuego',views.agregar_videojuego, name = "agregar_videojuego"),

    #agregar consola
    path('agregar_consola', views.agregar_consola, name="agregar_consola"),
]