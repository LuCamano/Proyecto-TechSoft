from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginV, name="login"),
    path('marcas/', views.marcas, name="marcas"),
    path('categorias/', views.categorias, name="categorias"),
    path('producto/', views.producto, name="producto"),
    path('productos/', views.productos, name="productos"),
    path('administracion/', views.administracion, name="administracion"),
    path('administracion/productos/', views.adminProductos, name="admin-productos"),
    path('administracion/productos/<id>/caracteristicas/', views.caractProducto, name="caracteristicas-producto"),
    path('administracion/categorias/', views.adminCategorias, name="admin-categorias"),
    path('administracion/marcas/', views.adminMarcas, name="admin-marcas"),
    path('administracion/caracteristicas/', views.adminCaracteristicas, name="admin-caracteristicas"),
    path('administracion/agregar-producto/', views.AgregarProducto.as_view(), name="agregar-producto"),
]
