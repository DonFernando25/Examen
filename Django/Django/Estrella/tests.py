from django.test import TestCase
from .models import Usuario, Producto  # Importa los modelos que usarás


class UsuarioModelTest(TestCase):
    def test_crear_usuario(self):
        usuario = Usuario.objects.create(
            nombre="Juan", apellido="Pérez", nombre_usuario="juanp", correo="juanp@example.com", contrasena="password123")
        self.assertEqual(usuario.nombre, "Juan")



class LoginTest(TestCase):
    def setUp(self):
        self.credentials = {
            'nombre_usuario': 'juanp',
            'contrasena': 'password123'
        }
        Usuario.objects.create(**self.credentials)

    def test_login(self):
        response = self.client.post('/Estrella/IniSe', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)


class CarritoTest(TestCase):
    def test_agregar_producto(self):
        producto = Producto.objects.create(nombre="Camiseta", precio=35000)
        response = self.client.post('/carrito/agregar', {'producto_id': producto.id})
        carrito = self.client.session['carrito']
        self.assertIn(str(producto.id), carrito)


import time

class CargaPaginaTest(TestCase):
    def test_tiempo_respuesta(self):
        start_time = time.time()
        self.client.get('/Estrella/Tienda')
        tiempo_respuesta = time.time() - start_time
        self.assertLess(tiempo_respuesta, 2)
