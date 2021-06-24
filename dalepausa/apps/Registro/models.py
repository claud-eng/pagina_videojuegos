from django.db import models

# Create your models here.

class Videojuego(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    formato = models.CharField(max_length=20)
    plataforma = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Consola(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField()
    stock = models.IntegerField()
    empresa = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
