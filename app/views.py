from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import UpdateView
from .models import Categoria, Producto, Carrito
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("inicio")
    template_name = "registration/signup.html"

class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    template_name = 'app/user_update.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Usuario actualizado correctamente')
        return reverse_lazy("inicio")

    def get_object(self, queryset=None):
        return self.request.user


def inicio(request):
    categorias = Categoria.objects.all()
    return render(request, 'app/Inicio.html', { 'categorias': categorias })

def productos(request, id):
    productos = Producto.objects.filter(idCategoria=id)
    return render(request, 'app/Productos.html', { 'categoria': id, 'productos': productos})

def carrito(request):
    carrito, created = Carrito.objects.get_or_create(defaults= {'username': request.user }, username=request.user)
    carrito.save()

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

def perfil(request):

    return render(request, 'app/Perfil.html')

def user_update_success(request):
    return render(request, 'user_update_success.html')