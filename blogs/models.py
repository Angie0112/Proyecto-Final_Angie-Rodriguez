from django.db import models

# Modelo para Artículo
class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='imagenes_articulos/', null=True, blank=True)

    def __str__(self):
        return f'Este post se llama {self.titulo} y fue escrito por {self.autor} en la fecha {self.fecha}'
