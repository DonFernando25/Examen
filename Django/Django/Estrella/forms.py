from django import forms
from .models import Producto
from .models import Admin

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre', 'categoria', 'descripcion', 'stock_talla_s', 
            'stock_talla_m', 'stock_talla_l', 'stock_talla_xl', 
            'precio', 'fotografia', 'url_compra'
        ]


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['nombre_usuario', 'correo', 'contrasena']