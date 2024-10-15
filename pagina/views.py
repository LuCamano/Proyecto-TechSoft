from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def marcas(request):
    return render(request, "marcas.html")

def categorias(request):
    return render(request, "categorias.html")

def producto(request):
    return render(request, "producto.html")

def productos(request):
    return render(request, "productos.html")

def administracion(request):
    return render(request, "administracion.html")