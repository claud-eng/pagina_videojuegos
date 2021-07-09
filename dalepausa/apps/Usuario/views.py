from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import UsuarioForm

# Create your views here.

class UsuarioCreate(CreateView):
    model = User
    template_name = "Usuario/registrar_usuario.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')


class UsuarioList(ListView):
    model = User
    template_name = 'Usuario/listar_usuarios.html'
