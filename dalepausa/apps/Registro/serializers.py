from rest_framework import serializers
from .models import Videojuego, Consola

class VideojuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videojuego
        fields = ('nombre','precio','stock','formato','plataforma')


class ConsolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consola
        fields = '__all__'
