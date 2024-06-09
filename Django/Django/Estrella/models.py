from django.db import models


# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nombre_usuario = models.CharField(max_length=50, unique=True)
    correo = models.EmailField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"