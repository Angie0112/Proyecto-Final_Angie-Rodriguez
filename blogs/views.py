from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse

from blogs.forms import FormularioArticulo
from .models import Articulo
from django.template import loader

from django.views.generic import ListView
# Create your views here.

def listar_articulos(request):
    contexto = { 
        "articulos": Articulo.objects.all(),
        "userIsAuthenticated": request.user.is_authenticated,
        "user": request.user,
    }
    http_response = render(
        request=request,
        template_name='blogs/lista_articulos.html',
        context=contexto,
    )
    return http_response

# C = CREATE
def crear_articulo(request):
    if request.method == "POST":
        formulario = FormularioArticulo(request.POST, request.FILES)

        if request.user.is_authenticated:
            autor = request.user
            if formulario.is_valid():
                articulo = formulario.save(commit=False)
                articulo.autor = autor
                articulo.save()

                # Redireccionar al usuario a la lista de artículos
                url_exitosa = reverse('articulos')  # estudios/articulos/
                return redirect(url_exitosa)
    else:  # GET
        formulario = FormularioArticulo()
    
    http_response = render(
        request=request,
        template_name='blogs/crear_editar_articulo.html',
        context={'form': formulario}
    )
    return http_response

# R = READ
def detalle_articulo(request, articulo_id):
    articulo = Articulo.objects.get(id=articulo_id)
    http_response = render(
        request=request,
        template_name='blogs/detalle_articulo.html',
        context={'articulo': articulo}
    )
    return http_response

# U = UPDATE
def editar_articulo(request, articulo_id):
    articulo = Articulo.objects.get(id=articulo_id)
    if request.method == "POST":
        formulario = FormularioArticulo(request.POST, request.FILES, instance=articulo)

        if formulario.is_valid():
            articulo = formulario.save()

            # Redireccionar al usuario a la lista de artículos
            url_exitosa = reverse('articulos')  # estudios/articulos/
            return redirect(url_exitosa)
    else:  # GET
        formulario = FormularioArticulo(instance=articulo)
    
    http_response = render(
        request=request,
        template_name='blogs/crear_editar_articulo.html',
        context={'form': formulario}
    )
    return http_response

# D = DELETE
def eliminar_articulo(request, articulo_id):
    articulo = Articulo.objects.get(id=articulo_id)
    articulo.delete()
    url_exitosa = reverse('articulos')
    return redirect(url_exitosa)


