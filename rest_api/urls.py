from django.urls import path
from . import views

#api/
urlpatterns = [
    path('Productos/', views.lista_Productos, name='lista_Productos'),
    path('Productos/<id>', views.vista_Producto, name='vista_Producto'),
]