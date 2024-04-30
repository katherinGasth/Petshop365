from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Categoria, Producto, Carrito
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator



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

    return render(request, 'app/Carrito.html', { 'items': carrito.items.all() })

def add_carrito(request):
    if request.method == "POST":
        idProducto = request.POST.get("id")
        cantidad = request.POST.get("cantidad")
        
        carrito, created = Carrito.objects.get_or_create(defaults= {'username': request.user, 'productos': [] }, username=request.user)
        producto = Producto.objects.get(idProducto=idProducto)

        itemCarrito = ItemCarrito.objects.create(cantidad = cantidad, producto=producto)

        carrito.items.add(itemCarrito)
        carrito.save()
        messages.success(request, producto.nombreProducto + " agregado al carrito.")

    return redirect(to=request.META.get('HTTP_REFERER'))

def del_carrito(request):
    if request.method == "POST":
        idItem = request.POST.get("id")

        carrito, created = Carrito.objects.get_or_create(defaults= {'username': request.user, 'items': [] }, username=request.user)
        carrito.items.remove(carrito.items.get(id=idItem))
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
