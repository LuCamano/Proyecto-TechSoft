from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import ProductoForm, LoginForm, ProductoCaracteristicaForm
from .models import Producto, Marca, Categoria, Caracteristica
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.contrib import messages
# Create your views here.

def index(request):
    lista_productos = Producto.objects.all().order_by('-id')[:10]
    context = {'productos': lista_productos}
    return render(request, "index.html", context)

class LoginV(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

@login_required
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

@login_required
def adminProductos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, "administracion_productos.html", context)

@login_required
def adminCaracteristicas(request):
    caracts = Caracteristica.objects.all()
    context = { 'caracteristicas': caracts }
    return render(request, "administracion_caracteristicas.html", context)

@login_required
def adminMarcas(request):
    marcas = Marca.objects.all()
    context = { 'marcas': marcas }
    return render(request, "administracion_marcas.html", context)

@login_required
def adminCategorias(request):
    categs = Categoria.objects.all()
    context = { 'categorias': categs }
    return render(request, "administracion_categorias.html", context)

@login_required
def administracion(request):
    return redirect('/administracion/productos')

@login_required
def caractProducto(request, id):
    producto = Producto.objects.get(id=id)
    context = {
        'producto': producto.nombre,
        'caracteristicas': producto.caracteristicas,
        'urlAnterior': '/administracion/productos/'
    }
    return render(request, "caracteristicas_producto.html", context)

class AgregarProducto(LoginRequiredMixin, CreateView):
    template_name = "formulario.html"
    form_class = ProductoForm
    success_url = '/administracion/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar Producto'
        context['urlAnterior'] = '/administracion/'
        return context
    
@login_required
def asignarCaracteristicas(request:HttpRequest, idP):
    if request.method == "POST":
        form = ProductoCaracteristicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administracion')
    product = Producto.objects.get(id=idP)
    form = ProductoCaracteristicaForm(producto=product)
    context = { 
        'form': form,
        'titulo': 'Agregar una característica',
        'urlAnterior': '/administracion/'
        }
    return render(request, "formulario.html", context)