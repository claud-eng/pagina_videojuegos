from django.shortcuts import render,redirect
from .models import Videojuego,Consola
from .forms import VideojuegoForm,ConsolaForm

# Create your views here.

def listar_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request,"Registro/listar_videojuegos.html", {'videojuegos': videojuegos})


def agregar_videojuego(request):
    if request.method == "POST":
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_videojuego")
    else:
        form = VideojuegoForm()
        return render(request, "Registro/agregar_videojuego.html", {'form': form})


def agregar_consola(request):
    if request.method == "POST":
        form = ConsolaForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_consola")
    else:
        form = ConsolaForm()
        return render(request, "Registro/agregar_consola.html", {'form': form})

