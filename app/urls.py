from django.urls import path
from .views import inicio, productos, SignUpView, carrito, add_carrito, del_carrito, recuperar
from django.urls import path
from . import views

urlpatterns = [
    path('', inicio, name='inicio'),
    path('carrito', carrito, name="carrito"),
    path('carrito/add', add_carrito, name="add_carrito"),
    path('carrito/delete', del_carrito, name="del_carrito"),
    path('accounts/signup/', SignUpView.as_view(), name="signup"),
    path('productos/<int:id>', productos, name="productos"), 
    path('recuperar/', recuperar, name='recuperar'),
    path('recuperar/', views.recuperar, name='recuperar'),
]
