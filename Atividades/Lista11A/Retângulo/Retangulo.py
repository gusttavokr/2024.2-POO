import math

class Retangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def getBase(self):
        return self.__base
    def setBase(self, base):
        if base > 0:
            self.__base = base
        else:
            raise ValueError('Base negativa inválida')
        
    def getAltura(self):
        return self.__altura
    def setAltura(self, altura):
        if altura > 0:
            self.__altura = altura
        else:
            raise ValueError('Altura negativa inválida')

    def CalcArea(self):
        area = self.__altura*self.__base
        return area

    def CalcDiag(self):
        Diag = math.sqrt((self.__altura*self.__altura)+(self.__base*self.__base))
        Diag = "{:.2f}".format(Diag)
        return Diag

    def __str__(self):
        return f"{self.__base} - {self.__altura} - {self.CalcArea()} - {self.CalcDiag()}"

class Quadrado(Retangulo):
    def __init__(self, base):
        super().__init__(base, base)
    
    def __str__(self):
        return f"{self.__base} - {self.CalcArea()} - {self.CalcDiag()}"