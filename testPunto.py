from unittest import TestCase
from punto import punto

class Test(TestCase):
    def test_punto(self):
        a = punto(1, 0)
        b = punto(-1, 0)
        dist = a.hallarDistancia(b)
        self.assertEqual(dist,2)