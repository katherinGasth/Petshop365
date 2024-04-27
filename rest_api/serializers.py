from rest_framework import serializers
from app.models import Producto, Categoria

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields = ['idProducto', 'idCategoria', 'nombreProducto', 'precioProducto', 'stock_producto', 'rutaImagen']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields = ['idCategoria', 'nombreCategoria', 'descripcionCategoria', 'rutaImagen']