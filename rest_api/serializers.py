from rest_framework import serializers
from app.models import Producto, Categoria

class ProductoSerializer(serializers.modelSerializer):
    class Meta:
        model=Producto
        fields = ['idProducto', 'idCategoria', 'nombreProducto', 'precioProducto', 'stock_producto', 'rutaImagen']

class CategoriaSerializer(serializers.modelSerializer):
    class Meta:
        model=Categoria
        fields = ['idCategoria', 'nombreCategoria', 'descripcionCategoria', 'rutaImagen']