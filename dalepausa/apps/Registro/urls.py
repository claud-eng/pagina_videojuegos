from django.urls import path,include
from . import views

urlpatterns = [
    
    #lista de video juegos
    path('listar_videojuegos', views.VideojuegoList.as_view(), name = "listar_videojuegos"),

    #agregar videojuego
    path('agregar_videojuego',views.VideojuegoCreate.as_view(), name = "agregar_videojuego"),

    #borrar videojuego
    path('eliminar_videojuego/<int:pk>', views.VideojuegoDelete.as_view(), name = "eliminar_videojuego"),

    #modificar videojuego
    path('modificar_videojuego/<int:pk>', views.VideojuegoUpdate.as_view(), name = "modificar_videojuego"),



    #lista de consola
    path('listar_consolas', views.ConsolaList.as_view(), name = "listar_consolas"),

    #agregar consola
    path('agregar_consola', views.ConsolaCreate.as_view(), name="agregar_consola"),

    #borrar videojuego
    path('eliminar_consola/<int:pk>', views.ConsolaDelete.as_view(), name = "eliminar_consola"),

    #modificar videojuego
    path('modificar_consola/<int:pk>', views.ConsolaUpdate.as_view(), name = "modificar_consola"),

]