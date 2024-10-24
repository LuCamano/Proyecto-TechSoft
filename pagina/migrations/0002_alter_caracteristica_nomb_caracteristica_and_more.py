# Generated by Django 5.1.2 on 2024-10-23 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristica',
            name='nomb_caracteristica',
            field=models.CharField(max_length=45, unique=True, verbose_name='Característica'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nomb_categoria',
            field=models.CharField(max_length=45, unique=True, verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='nomb_marca',
            field=models.CharField(max_length=45, unique=True, verbose_name='Marca'),
        ),
    ]
