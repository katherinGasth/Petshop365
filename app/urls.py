from django.urls import path
from .views import inicio, productos, SignUpView, carrito, add_carrito, del_carrito, perfil, user_update_success
from .views import UserUpdateView

urlpatterns = [
    path('', inicio, name='inicio'),
    path('carrito', carrito, name="carrito"),
    path('carrito/add', add_carrito, name="add_carrito"),
    path('carrito/delete', del_carrito, name="del_carrito"),
    path('accounts/signup/', SignUpView.as_view(), name="signup"),
    path('productos/<int:id>', productos, name="productos"),
    path('perfil', perfil, name="perfil"),
    path('update/', UserUpdateView.as_view(), name='user_update'),
    path('update/success/', user_update_success, name='user_update_success'),
]
