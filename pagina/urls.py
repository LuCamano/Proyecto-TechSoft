from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('marcas/', views.marcas, name="marcas"),
    path('categorias/', views.categorias, name="categorias"),
    path('producto/', views.producto, name="producto"),
    path('productos/', views.productos, name="productos"),
    path('administracion/', views.administracion, name="administracion"),
]
