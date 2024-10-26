from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from .forms import ProductoForm, LoginForm, ProductoCaracteristicaForm, CaracteristicaForm, MarcaForm, CategoriaForm
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
    marcs = Marca.objects.all()
    context = {
        'marcas': marcs
    }
    return render(request, "marcas.html", context)

def categorias(request):
    categs = Categoria.objects.all()
    context = {
        'categorias': categs
    }
    return render(request, "categorias.html", context)

def producto(request, id):
    context = {
        'producto': Producto.objects.get(id=id)
    }
    return render(request, "producto.html", context)

def productos(request):
    products = Producto.objects.all()
    context = {
        'productos': products
    }
    return render(request, "productos.html", context)

@login_required
def adminProductos(request):
    productos = Producto.objects.all().order_by('-id')
    context = {
        'productos': productos
    }
    return render(request, "administracion_productos.html", context)

@login_required
def adminCaracteristicas(request):
    caracts = Caracteristica.objects.all().order_by('-id')
    context = { 'caracteristicas': caracts }
    return render(request, "administracion_caracteristicas.html", context)

@login_required
def adminMarcas(request):
    marcas = Marca.objects.all().order_by('-id')
    context = { 'marcas': marcas }
    return render(request, "administracion_marcas.html", context)

@login_required
def adminCategorias(request):
    categs = Categoria.objects.all().order_by('-id')
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
    
class AgregarCaracteristica(LoginRequiredMixin, CreateView):
    template_name = "formulario.html"
    form_class = CaracteristicaForm
    success_url = '/administracion/caracteristicas'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar Característica'
        context['urlAnterior'] = '/administracion/caracteristicas'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Característica agregada correctamente')
        return super().form_valid(form)
    
class EditarCaracteristica(LoginRequiredMixin,UpdateView):
    model = Caracteristica
    form_class = CaracteristicaForm
    template_name = "formulario.html"
    success_url = '/administracion/caracteristicas'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Característica'
        context['urlAnterior'] = '/administracion/caracteristicas'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Característica editada correctamente')
        return super().form_valid(form)
    
@login_required
def eliminarCaracteristica(request, id):
    caract = Caracteristica.objects.get(id=id)
    try:
        caract.delete()
        messages.success(request, 'Característica eliminada correctamente')
    except Exception as e:
        messages.warning(request, 'Error: La característica no se puede eliminar (es posible que tenga otros elementos asociados)')
    return redirect('/administracion/caracteristicas')

class AgregarMarca(LoginRequiredMixin, CreateView):
    template_name = "formulario.html"
    form_class = MarcaForm
    success_url = '/administracion/marcas'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar Marca'
        context['urlAnterior'] = '/administracion/marcas'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Marca agregada correctamente')
        return super().form_valid(form)

class EditarMarca(LoginRequiredMixin, UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = "formulario.html"
    success_url = '/administracion/marcas'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Marca'
        context['urlAnterior'] = '/administracion/marcas'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Marca editada correctamente')
        return super().form_valid(form)
    
@login_required
def eliminarMarca(request, id):
    marca = Marca.objects.get(id=id)
    try:
        marca.delete()
        messages.success(request, 'Marca eliminada correctamente')
    except Exception as e:
        messages.warning(request, 'Error: La marca no se puede eliminar (es posible que tenga otros elementos asociados)')
    return redirect('/administracion/marcas')

class AgregarCategoria(LoginRequiredMixin, CreateView):
    template_name = "formulario.html"
    form_class = CategoriaForm
    success_url = '/administracion/categorias'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar Categoría'
        context['urlAnterior'] = '/administracion/categorias'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Categoría agregada correctamente')
        return super().form_valid(form)

class EditarCategoria(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "formulario.html"
    success_url = '/administracion/categorias'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Categoría'
        context['urlAnterior'] = '/administracion/categorias'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Categoría editada correctamente')
        return super().form_valid(form)
    
@login_required
def eliminarCategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    try:
        categoria.delete()
        messages.success(request, 'Categoría eliminada correctamente')
    except Exception as e:
        messages.warning(request, 'Error: La categoría no se puede eliminar (es posible que tenga otros elementos asociados)')
    return redirect('/administracion/categorias')