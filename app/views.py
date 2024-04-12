from django.shortcuts import render
from .models import Categoria

# Create your views here.

def inicio(request):
    categorias = Categoria.objects.all()
    return render(request, 'app/Inicio.html', { 'categorias': categorias })

def alimentos(request):
    return render(request, 'app/Alimentos.html')

def snacks(request):
    return render(request, 'app/Snacks.html')


def accesorios(request):
    return render(request, 'app/Accesorios.html')


def formulario(request):
    return render(request, 'app/FormularioDeRegistro.html')

def cuidadoSalud(request):
    return render(request, 'app/cuidadoSalud.html')

def juguetes(request):
    return render(request, 'app/Juguetes.html')



def vestimenta(request):
    return render(request, 'app/Vestimenta.html')

