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
    



class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    descripcion = models.TextField()
    stock_talla_s = models.PositiveIntegerField(default=0)
    stock_talla_m = models.PositiveIntegerField(default=0)
    stock_talla_l = models.PositiveIntegerField(default=0)
    stock_talla_xl = models.PositiveIntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fotografia = models.ImageField(upload_to='productos/')
    url_compra = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre
    


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_usuario