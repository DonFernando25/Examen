from django.db import models


# Create your models here.



class Usuario(models.Model):
    MASCULINO = 'M'
    FEMENINO = 'F'
    OTRO = 'O'

    GENERO_CHOICES = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
        (OTRO, 'Otro'),
    ]

    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    nombre_usuario = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.nombre_usuario})"