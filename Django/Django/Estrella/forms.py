from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre', 'categoria', 'descripcion', 'stock_talla_s', 
            'stock_talla_m', 'stock_talla_l', 'stock_talla_xl', 
            'precio', 'fotografia', 'url_compra'
        ]
