from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import ProductoForm, LoginForm, ProductoCaracteristicaForm
from .models import Producto, Marca, Categoria, Caracteristica, ProductoCaracteristica
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
    productos = Producto.objects.all().order_by('-id')
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
        'idP': id,
        'caracteristicas': producto.caracteristicas,
        'urlAnterior': '/administracion/productos/'
    }
    return render(request, "caracteristicas_producto.html", context)

class AgregarProducto(LoginRequiredMixin, CreateView):
    template_name = "formulario.html"
    form_class = ProductoForm
    success_url = '/administracion/productos'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar Producto'
        context['urlAnterior'] = '/administracion/productos'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Producto agregado correctamente')
        return super().form_valid(form)
    
@login_required
def editarProducto(request, pk):
    product = Producto.objects.get(id=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto editado correctamente')
            return redirect('/administracion/productos')
        else:
            messages.warning(request, 'Error al editar el producto')
    form = ProductoForm(instance=product)
    context = {
        'form': form,
        'titulo': 'Editar Producto',
        'urlAnterior': '/administracion/productos'
    }
    return render(request, "formulario.html", context)

@login_required
def eliminarProducto(request, pk):
    product = Producto.objects.get(id=pk)
    try:
        product.delete()
        messages.success(request, 'Producto eliminado correctamente')
    except Exception as e:
        messages.warning(request, 'Error: El producto no se puede eliminar (es posible que tenga otros elementos asociados)')
    return redirect('/administracion/productos')

@login_required
def asignarCaracteristicas(request:HttpRequest, idP):
    product = Producto.objects.get(id=idP)
    if request.method == "POST":
        form = ProductoCaracteristicaForm(request.POST)
        if form.is_valid():
            form.instance.producto = product
            print(form.instance)
            form.save()
            return redirect(f'/administracion/productos/{idP}/caracteristicas/')
    form = ProductoCaracteristicaForm()
    context = { 
        'form': form,
        'titulo': f'Agregar una característica a {product.nombre}',
        'urlAnterior': f'/administracion/productos/{idP}/caracteristicas/'
        }
    return render(request, "formulario.html", context)

@login_required
def editarCaracteristicaProducto(request, idP, idCP):
    caractProd = ProductoCaracteristica.objects.get(id=idCP)
    if request.method == "POST":
        form = ProductoCaracteristicaForm(request.POST, instance=caractProd)
        if form.is_valid():
            form.save()
            return redirect(f'/administracion/productos/{idP}/caracteristicas/')
    form = ProductoCaracteristicaForm(instance=caractProd)
    context = {
        'form': form,
        'titulo': f'Editar característica de {caractProd.producto.nombre}',
        'urlAnterior': f'/administracion/productos/{idP}/caracteristicas/'
    }
    return render(request, "formulario.html", context)

@login_required
def eliminarCaracteristicaProducto(request, idP, idCP):
    caractProd = ProductoCaracteristica.objects.get(id=idCP)
    nombre = caractProd.caracteristica.nomb_caracteristica
    try:
        caractProd.delete()
        messages.success(request, f'Característica {nombre} eliminada correctamente')
    except Exception as e:
        messages.warning(request, f'Error: {e}')
    return redirect(f'/administracion/productos/{idP}/caracteristicas/')
    