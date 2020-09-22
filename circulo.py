from figura import figura
class circulo(figura):
        pass

        def determinarEnElCirculo(self, p):
                centro = self.punto[0]
                radio = self.punto[1]
                return centro.hallarDistancia(p)<=centro.hallarDistancia(radio)