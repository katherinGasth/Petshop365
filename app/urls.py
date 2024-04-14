from django.urls import path
from .views import inicio, productos, SignUpView, carrito, add_carrito, del_carrito

urlpatterns = [
    path('', inicio, name='inicio'),
    path('carrito', carrito, name="carrito"),
    path('carrito/add', add_carrito, name="add_carrito"),
    path('carrito/delete', del_carrito, name="del_carrito"),
    path('accounts/signup/', SignUpView.as_view(), name="signup"),
    path('productos/<int:id>', productos, name="productos")
]
