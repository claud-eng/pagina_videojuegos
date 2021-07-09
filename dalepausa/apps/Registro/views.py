from django.shortcuts import render,redirect
from .models import Videojuego,Consola
from .forms import VideojuegoForm,ConsolaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

#--token
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User



# las importaciones para la API 
from rest_framework import generics
from .serializers import VideojuegoSerializer,ConsolaSerializer


#------------- importacines API ---------------------
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404

from rest_framework import status

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 


#VIDEOJUEGOS
@api_view(['GET', 'POST'])
def videojuego_collection(request):
    if request.method == 'GET':
        videojuegos = Videojuego.objects.all()
        serializer = VideojuegoSerializer(videojuegos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VideojuegoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def videojuego_element(request, pk):
    videojuego = get_object_or_404(Videojuego, id=pk)

    if request.method == 'GET':
        serializer = VideojuegoSerializer(videojuego)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        videojuego.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        videojuego_new = JSONParser().parse(request) 
        serializer = VideojuegoSerializer(videojuego, data=videojuego_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#CONSOLAS
@api_view(['GET'])
def consola_collection(request):
    if request.method == 'GET':
        consolas = Consola.objects.all()
        serializer = ConsolaSerializer(consolas, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def consola_element(request, pk):
    consola = get_object_or_404(Consola, id=pk)

    if request.method == 'GET':
        serializer = ConsolaSerializer(consola)
        return Response(serializer.data)


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


#---------------------- ASIGNAR TOKEN------------------------
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

