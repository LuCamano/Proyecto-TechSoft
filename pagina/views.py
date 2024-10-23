from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from .forms import ProductoForm
from .models import Producto, Marca, Categoria, Caracteristica
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    lista_productos = Producto.objects.all().order_by('-id')[:10]
    context = {'productos': lista_productos}
    return render(request, "index.html", context)

def loginV(request):
    return render(request, "login.html")

def logoutV(request):
    logout(request)
    return redirect('/')

def marcas(request):
    return render(request, "marcas.html")

def categorias(request):
    return render(request, "categorias.html")

def producto(request):
    return render(request, "producto.html")

def productos(request):
    return render(request, "productos.html")

def adminProductos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, "administracion_productos.html", context)

def adminCaracteristicas(request):
    caracts = Caracteristica.objects.all()
    context = { 'caracteristicas': caracts }
    return render(request, "administracion_caracteristicas.html", context)

def adminMarcas(request):
    marcas = Marca.objects.all()
    context = { 'marcas': marcas }
    return render(request, "administracion_marcas.html", context)

def adminCategorias(request):
    categs = Categoria.objects.all()
    context = { 'categorias': categs }
    return render(request, "administracion_categorias.html", context)

def administracion(request):
    return redirect('/administracion/productos')

def caractProducto(request, id):
    producto = Producto.objects.get(id=id)
    context = {
        'producto': producto.nombre,
        'caracteristicas': producto.caracteristicas,
        'urlAnterior': '/administracion/productos/'
    }
    return render(request, "caracteristicas_producto.html", context)

class AgregarProducto(CreateView, LoginRequiredMixin):
    template_name = "formulario.html"
    form_class = ProductoForm
    success_url = '/administracion/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar Producto'
        context['urlAnterior'] = '/administracion/'
        return context