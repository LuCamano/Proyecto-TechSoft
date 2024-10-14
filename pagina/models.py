from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField("Nombre", max_length=45)
    precio = models.IntegerField("Precio")
    stock = models.IntegerField("Stock")
    marca = models.ForeignKey('Marca', verbose_name="Marca", on_delete=models.PROTECT)
    categoria = models.ForeignKey('Categoria', verbose_name="Categoría", on_delete=models.PROTECT)
class Categoria(models.Model):
    nomb_categoria = models.CharField("Categoría", max_length=45)
    
class Marca(models.Model):
    nomb_marca = models.CharField("Marca", max_length=45)
    
class Caracteristica(models.Model):
    nomb_caracteristica = models.CharField("Característica", max_length=45)
    
class ProductoCaracteristica(models.Model):
    producto = models.ForeignKey('Producto', verbose_name="Producto", on_delete=models.PROTECT)
    caracteristica = models.ForeignKey('Caracteristica', verbose_name="Característica", on_delete=models.PROTECT)
    descripcion_caract = models.CharField("Descripción", max_length=45)