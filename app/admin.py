from django.contrib import admin

from .models import Categoria, Producto, Cliente, Compra

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Compra)