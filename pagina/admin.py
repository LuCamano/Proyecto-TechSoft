from django.contrib import admin
from .models import Caracteristica, Producto, Marca, Categoria, ProductoCaracteristica

# Register your models here.

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nomb_marca']
    
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nomb_categoria']
    
@admin.register(Caracteristica)
class CaracteristicaAdmin(admin.ModelAdmin):
    list_display = ['nomb_caracteristica']
    
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock', 'marca', 'categoria']
    
@admin.register(ProductoCaracteristica)
class ProductoCaracteristicaAdmin(admin.ModelAdmin):
    list_display = ['producto', 'caracteristica', 'descripcion_caract']
    list_filter = ['producto', 'caracteristica']