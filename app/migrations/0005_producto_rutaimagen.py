# Generated by Django 5.0.3 on 2024-04-12 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_cliente_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='rutaImagen',
            field=models.CharField(default='x', max_length=200, verbose_name='Imagen Producto'),
            preserve_default=False,
        ),
    ]
