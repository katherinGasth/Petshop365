from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria') 
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la cotegoria')
    descripcionCategoria = models.CharField(max_length=500, verbose_name='Descripcion categoria')
    rutaImagen = models.CharField(max_length=200, verbose_name='Imagen categoria')

    def __str__(self):
        return self.nombreCategoria
    
class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id del producto')
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombreProducto = models.CharField(max_length=50, verbose_name='Nombre del producto')
    precioProducto = models.IntegerField(verbose_name='Precio del producto')
    stock_producto = models.IntegerField(verbose_name='Stock del producto')
    rutaImagen = models.CharField(max_length=200, verbose_name='Imagen Producto')

    def __str__(self):
        return self.nombreProducto


class Cliente(models.Model):
    rutCliente = models.IntegerField(primary_key=True, verbose_name='Rut del cliente')
    nombreCliente = models.CharField(max_length=150, verbose_name='Nombre del cliente')
    correoElectronico = models.CharField(max_length=50, verbose_name='Correo del cliente')
    claveSeguridad = models.CharField(max_length=50, verbose_name='Clave del cliente')
    fechaNacimiento = models.CharField(max_length=50, verbose_name='Fecha de nacimiento del cliente')
    direccionCliente = models.CharField(max_length=150, verbose_name='Direccion del cliente')

    def __str__(self):
        return self.nombreCliente


class Compra(models.Model):
    idCompra = models.IntegerField(primary_key=True, verbose_name='Id de la compra')
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(verbose_name="Fecha de compra")
    productos = models.ManyToManyField(Producto)

    def __str__(self):
        return self.idCompra

class Carrito(models.Model):
    username = models.CharField(max_length=50, verbose_name='Username del cliente')
    productos = models.ManyToManyField(Producto)
