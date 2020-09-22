from unittest import TestCase

from circulo import circulo
from punto import punto
from figura import figura
from rectangulo import rectangulo
from triangulo import triangulo


class Test(TestCase):
    def test_figuraCirculo(self):
        a=punto(0,1)
        b=punto(0,6)
        z=[a,b]
        circulo = circulo(z)
        p= circulo.hallarPerimetro()
        self.assertAlmostEqual(p, 25.13, places=1)
        ar= circulo.hallarArea()
        self.assertAlmostEqual(ar, 50.26, places=1)

    def test_figuraTriangulo(self):
        a=punto(0,0)
        b=punto(2,0)
        c=punto(0,2)
        z=[a,b,c]
        triangulo= triangulo(z)
        p= triangulo.hallarPerimetro()
        self.assertAlmostEqual(p, 6.8, places=1)
        ar= triangulo.hallarArea()
        self.assertAlmostEqual(ar, 2, places=1)

    def test_figuraRectangulo(self):
        a=punto(1,1)
        b=punto(4,1)
        c=punto(4,3)
        d=punto(1,3)
        z=[a,b,c,d]
        rectangulo = rectangulo(z)
        p = rectangulo.hallarPerimetro()
        self.assertAlmostEqual(p, 10, places=1)
        ar = rectangulo.hallarArea()
        self.assertAlmostEqual(ar, 6, places=1)
