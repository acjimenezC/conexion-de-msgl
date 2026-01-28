from django.test import TestCase
from .models import Nombre

class NombreTest(TestCase):
    def test_crear_nombre(self):
        nombre = Nombre.objects.create(nombre='Juan')
        self.assertEqual(nombre.nombre, 'Juan')
