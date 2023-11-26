from django import forms
from .models import *


class FormularioArticulo(forms.ModelForm):

    class Meta:
        model = Articulo
        exclude = ['autor']
