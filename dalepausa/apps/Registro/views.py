from django.shortcuts import render,redirect
from .models import Videojuego,Consola
from .forms import VideojuegoForm,ConsolaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

#VIDEOJUEGO

class VideojuegoList(ListView):
    model = Videojuego
    template_name = 'Registro/listar_videojuegos.html'


class VideojuegoCreate(CreateView):
    model = Videojuego
    form_class = VideojuegoForm
    template_name = 'Registro/videojuego_form.html'
    success_url = reverse_lazy('listar_videojuegos')


class VideojuegoDelete(DeleteView):
    model = Videojuego
    template_name = 'Registro/eliminar_videojuego.html'
    success_url = reverse_lazy('listar_videojuegos')


class VideojuegoUpdate(UpdateView):
    model = Videojuego
    form_class = VideojuegoForm
    template_name = 'Registro/videojuego_form.html'
    success_url = reverse_lazy('listar_videojuegos')


#CONSOLA

class ConsolaList(ListView):
    model = Consola
    template_name = 'Registro/listar_consolas.html'

class ConsolaCreate(CreateView):
    model = Consola
    form_class = ConsolaForm
    template_name = 'Registro/consola_form.html'
    success_url = reverse_lazy('listar_consolas')

class ConsolaDelete(DeleteView):
    model = Consola
    template_name = 'Registro/eliminar_consola.html'
    success_url = reverse_lazy('listar_consolas')


class ConsolaUpdate(UpdateView):
    model = Consola
    form_class = ConsolaForm
    template_name = 'Registro/consola_form.html'
    success_url = reverse_lazy('listar_consolas')
