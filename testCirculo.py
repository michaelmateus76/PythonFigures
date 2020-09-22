from unittest import TestCase

from circulo import circulo
from punto import punto

a = punto(0, 2)
b = punto(0, 6)
c = [a, b]
circulo = circulo(c)

class Test(TestCase):

    def test_EnElcirculoTrue(self):
        z = punto(2,2)
        self.assertTrue(circulo.determinarEnElCirculo(z))

    def test_EnElCirculoFalse(self):
        w = punto(5, 5)
        self.assertFalse(circulo.determinarEnElCirculo(w))