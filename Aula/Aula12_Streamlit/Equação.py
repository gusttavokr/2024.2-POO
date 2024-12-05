import math

class Equação:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

        if a == 0:
            raise ValueError("Valor A inválido")

    def getA(self):
        return self.__a
    def setA(self, a):
        if a != 0:
            self.__a = a
        else:
            raise ValueError("Valor A inválido")
    
    def getB(self):
        return self.__b
    def setB(self, b):
        self.__b = b
    
    def getC(self):
        return self.__c
    def setC(self, c):
        self.__c = c
        
    def __str__(self):
        return f"A = {self.__a} - B = {self.__b} - C = {self.__c}"
    
    def delta(self):
        delt = ((self.__b**2) - ((4*self.__a)*self.__c))
        return delt

    def x1(self, delta):
        if self.delta()>= 0:
            return (-(self.__b) - math.sqrt(delta)) / (2*self.__a)
        return None

    def x2(self, delta):
        if self.delta()>=0:
            return (-(self.__b) + math.sqrt(delta)) / (2*self.__a)
        return None

    def Y(self, x):
        return (self.__a*(x**2)) + (self.__b * x) + self.__c
    
    def xplano(self):
        return -self.__b / (2*self.__a)