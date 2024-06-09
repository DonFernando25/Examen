from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'nombre_usuario', 'correo', 'contrasena', 'fecha_nacimiento', 'genero']