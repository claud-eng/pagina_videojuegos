from django.urls import path,include
from . import views

#para la api
from rest_framework.urlpatterns import format_suffix_patterns
from apps.Registro import views



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

    # api videojuegos
    path('videojuegos/',  views.videojuego_collection , name='videojuego_collection'),
    path('videojuegos/<int:pk>/', views.videojuego_element ,name='videojuego_element'),

    # api consolas
    path('consolas/',  views.consola_collection , name='consola_collection'),
    path('consolas/<int:pk>/', views.consola_element ,name='consola_element'),

]

# #se le agrega el "+" para añadirles las rutas y así llamar a las funciones
# urlpatterns += [
#     path('api/', views.API_objects.as_view()),
#     path('api/<int:pk>/', views.API_objects_details.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)




