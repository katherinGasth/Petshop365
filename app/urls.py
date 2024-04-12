from django.urls import path
from .views import inicio, accesorios, alimentos, cuidadoSalud, juguetes, snacks, vestimenta, formulario

urlpatterns = [
    path('', inicio, name='inicio'),
    path('accesorios', accesorios, name='accesorios'),
    path('alimentos', alimentos, name='alimentos'),
    path('formulario', formulario, name='formulario'),
    path('cuidadoSalud', cuidadoSalud, name='cuidadoSalud'),
    path('juguetes', juguetes, name='juguetes'),
    path('snacks', snacks, name='snacks'),
    path('vestimenta', vestimenta, name='vestimenta'),
]
