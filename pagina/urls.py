from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.LoginV.as_view(), name="login"),
    path('logout/', views.logoutV, name="logout"),
    path('marcas/', views.marcas, name="marcas"),
    path('categorias/', views.categorias, name="categorias"),
    path('producto/', views.producto, name="producto"),
    path('productos/', views.productos, name="productos"),
    path('administracion/', views.administracion, name="administracion"),
    path('administracion/productos/', views.adminProductos, name="admin-productos"),
    path('administracion/productos/<id>/caracteristicas/', views.caractProducto, name="caracteristicas-producto"),
    path('administracion/productos/<idP>/caracteristicas/agregar/', views.asignarCaracteristicas, name="asignar-caracteristica"),
    path('administracion/productos/<idP>/caracteristicas/editar/<idCP>', views.editarCaracteristicaProducto, name="editar-caract-producto"),
    path('administracion/productos/<idP>/caracteristicas/eliminar/<idCP>', views.eliminarCaracteristicaProducto, name="eliminar-caract-producto"),
    path('administracion/categorias/', views.adminCategorias, name="admin-categorias"),
    path('administracion/marcas/', views.adminMarcas, name="admin-marcas"),
    path('administracion/caracteristicas/', views.adminCaracteristicas, name="admin-caracteristicas"),
    path('administracion/agregar-producto/', views.AgregarProducto.as_view(), name="agregar-producto"),
    path('administracion/editar-producto/<pk>', views.editarProducto, name="editar-producto"),
    path('administracion/eliminar-producto/<pk>', views.eliminarProducto, name="eliminar-producto"),
]
