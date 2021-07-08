from django.urls import path, include
from . import views
from .views import UsuarioCreate, UsuarioList



urlpatterns = [
    path('registrar_usuario', UsuarioCreate.as_view(), name="registrar_usuario"),
    path('listar_usuarios', UsuarioList.as_view(), name="listar_usuarios"),
]
