# Generated by Django 5.0.3 on 2024-04-15 18:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_carrito_idcliente_carrito_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='productos',
        ),
        migrations.CreateModel(
            name='ItemCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad de productos')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='items',
            field=models.ManyToManyField(to='app.itemcarrito'),
        ),
    ]
