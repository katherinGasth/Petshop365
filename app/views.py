from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Categoria, Producto, Carrito
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("inicio")
    template_name = "registration/signup.html"

def inicio(request):
    categorias = Categoria.objects.all() # Llamado a la base de datos
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

def recuperar(request):
    if request.method == "POST":
        email = request.POST['email']
        user = User.objects.filter(email=email).first()
        if user:
            # Generar un token único para el usuario y redirigirlo a la página de restablecimiento de contraseña
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            return redirect('password_reset_confirm', uidb64=uid, token=token)
        else:
            messages.error(request, 'No se encontró ninguna cuenta asociada a este correo electrónico.')
    return render(request, 'recuperar.html')

def password_reset_request(request):
    if request.method == "POST":
        email = request.POST['email']
        user = User.objects.filter(email=email).first()
        if user:
            # Generar un token único para el usuario y redirigirlo a la página de restablecimiento de contraseña
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            return redirect('password_reset_confirm.html', uidb64=uid, token=token)
        else:
            messages.error(request, 'No se encontró ninguna cuenta asociada a este correo electrónico.')
    return render(request, 'password_reset_request.html')

def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # Verificar que el token sea válido
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == "POST":
            password = request.POST['password']
            user.set_password(password)
            user.save()
            messages.success(request, 'Tu contraseña ha sido restablecida con éxito.')
            return redirect('login')
        return render(request, 'password_reset_confirm.html')
    else:
        messages.error(request, 'El enlace de restablecimiento de contraseña es inválido o ha caducado.')
        return redirect('login')

