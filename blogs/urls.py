from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_articulos, name='articulos'),
    path('articulos/', views.listar_articulos, name='articulos'),
    path('articulos/crear/', views.crear_articulo, name='nombre_crear_articulo'),
    path('articulos/<int:articulo_id>/', views.detalle_articulo, name='detalle_articulo'),
    path('articulos/<int:articulo_id>/editar/', views.editar_articulo, name='editar_articulo'),
    path('articulos/<int:articulo_id>/eliminar/', views.eliminar_articulo, name='eliminar_articulo'),
]