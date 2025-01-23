class Frete:
    def __init__(self, distancia, peso):
        self.__distancia = distancia
        self.__peso = peso

    def ValorFrete(self):
        produto = self.__distancia*self.__peso
        valor = "{:.02f}".format(produto*0.01)
        return valor
    
    def __str__(self):
        return f"{self.__distancia} - {self.__peso} - {self.ValorFrete()}"

class FreteExpresso(Frete):
    def __init__(self, distancia, peso, seguro):
        self.seguro = seguro
        super().__init__(distancia, peso)

    def ValorFrete(self):
        valor2 = super().ValorFrete()
        valorFinal = valor2 + (self.seguro * (1/100))
        return valorFinal
    
    def __str__(self):
        return super().__str__()