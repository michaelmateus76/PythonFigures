import math

from punto import punto

class figura():
    def __init__(self, punto1):
        self.punto = punto1

    def hallarPerimetro(self):
        n=len(self.punto)
        p=0
        if(n>2):
            for i in range(n):
                if(i== n-1):
                    p+= self.punto[i].hallarDistancia(self.punto[0])
                    i=n
                else:
                    p+= self.punto[i].hallarDistancia(self.punto[i+1])
        elif(n==2):
            p= 2* math.pi * self.punto[0].hallarDistancia(self.punto[1])
        print("El perimetro de la figura es: ",p)
        return p

    def areaCirculo(self):
        a=math.pi* math.pow(self.punto[0].hallarDistancia(self.punto[1]),2)
        print("El area del círculo es: ",a)
        return a

    def areaTriangulo(self):
        s= self.hallarPerimetro()/2
        a=math.sqrt(s*(s-self.punto[0].hallarDistancia(self.punto[1]))*(s-self.punto[1].hallarDistancia(self.punto[2]))* (s-self.punto[2].hallarDistancia(self.punto[0])))
        print("El area del triángulo es: ", a)
        return a

    def areaRectangulo(self):
        a= self.punto[0].hallarDistancia(self.punto[1]) * self.punto[1].hallarDistancia(self.punto[2])
        print("El area del rectángulo es: ",a)
        return a

    def hallarArea(self):
        n = len(self.punto)
        a = 0

        if(n==2):
            a= self.areaCirculo()
        elif(n==3):
            a= self.areaTriangulo()
        elif(n==4):
            a=self.areaRectangulo()

        return a


