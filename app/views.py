from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Categoria, Producto, Carrito


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("inicio")
    template_name = "registration/signup.html"

def inicio(request):
    categorias = Categoria.objects.all()
    return render(request, 'app/Inicio.html', { 'categorias': categorias })

def productos(request, id):
    productos = Producto.objects.filter(idCategoria=id)
    return render(request, 'app/Productos.html', { 'categoria': id, 'productos': productos})

def carrito(request):
    carrito, created = Carrito.objects.get_or_create(defaults= {'username': request.user, 'productos': [] }, username=request.user)
    return render(request, 'app/Carrito.html', { 'productos': carrito.productos.all() })

def add_carrito(request):
    if request.method == "POST":
        idProducto = request.POST.get("id")

        carrito, created = Carrito.objects.get_or_create(defaults= {'username': request.user, 'productos': [] }, username=request.user)
        producto = Producto.objects.get(idProducto=idProducto)

        carrito.productos.add(producto)
        carrito.save()
    return redirect(to="/carrito")

def del_carrito(request):
    if request.method == "POST":
        idProducto = request.POST.get("id")

        carrito, created = Carrito.objects.get_or_create(defaults= {'username': request.user, 'productos': [] }, username=request.user)
        carrito.productos.remove(carrito.productos.get(idProducto=idProducto))
        carrito.save()
    return redirect(to="/carrito")