from django import forms
from .models import Videojuego,Consola

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = ['nombre','precio','stock','formato','plataforma']

        labels = {
            'nombre': 'Nombre',
            'precio': 'Precio',
            'stock': 'Stock',
            'formato': 'Formato',
            'plataforma': 'Plataforma',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.TextInput(attrs={'class': 'form-control'}),
            'formato': forms.TextInput(attrs={'class': 'form-control'}),
            'plataforma': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ConsolaForm(forms.ModelForm):
    class Meta:
        model = Consola
        fields = ['nombre','precio', 'stock', 'empresa']

        labels = {
            'nombre': 'Nombre',
            'precio': 'Precio',
            'stock': 'Stock',
            'empresa': 'Empresa',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
            'stock': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'class':'form-control'}),
        }