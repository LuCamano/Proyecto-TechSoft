from django_filters import rest_framework as filters
from .models import Producto, Marca, Categoria

class ProductoFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains', label='Nombre')
    marca = filters.ModelChoiceFilter(queryset=Marca.objects.all(), label='Marca')
    categoria = filters.ModelChoiceFilter(queryset=Categoria.objects.all(), label='Categoria')
    
    precio_min = filters.NumberFilter(field_name='precio', lookup_expr='gte', label='Precio mínimo')
    precio_max = filters.NumberFilter(field_name='precio', lookup_expr='lte', label='Precio máximo')
    
    class Meta:
        model = Producto
        fields = ['nombre', 'marca', 'categoria', 'precio_min', 'precio_max']