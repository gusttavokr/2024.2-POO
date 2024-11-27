class Item:
    def __init__(self, produto, qtd, preco_unit):
        self.__produto = produto
        self.__qtd = qtd
        self.__precoUnit = preco_unit

        if produto == "":
            raise ValueError("Nome inválido")
        if qtd <= 0:
            raise ValueError("Quantidade insuficiente")
        if preco_unit <= 0:
            raise ValueError("Preço insuficiente")
        
    def getProduto(self):
        return self.__produto
    def setProduto(self, produto):
        self.__produto = produto
        if produto == "":
            raise ValueError("Nome inválido")
    
    def getQtd(self):
        return self.__qtd
    def setQtd(self, qtd):
        self.__qtd = qtd
        if qtd <= 0:
            raise ValueError("Quantidade insuficiente")
    
    def getPreco(self):
        return self.__precoUnit
    def setPreco(self, preco_unit):
        self.__precoUnit = preco_unit
        if preco_unit <= 0:
            raise ValueError("Preço insuficiente")
        
    def total(self):
        return self.__qtd * self.__precoUnit
    
    def __str__(self):
        return f"{self.__produto} - {self.__qtd} - {self.__precoUnit}"
        
class Carrinho:
    def __init__(self, cliente, data):
        self.__cliente = cliente
        self.__data = data
        self.__itens = []

    def inserir(self, item):
        self.__itens.append(item)
    def remover(self,item):
        self.__itens.remove(item)
    def listar(self):
        return self.__itens
    def total(self):
        t = 0
        for item in self.__itens:
            t += item.total()
        return t
    
    def __str__(self):
        return f"{self.__cliente} - {self.__data} - {len(self.__itens)} item(s)"


biscoito = Item("Treloso", 1, 3.5)
salgadinho = Item("Pippos", 2, 2.5)
salgadinho2 = Item("Cheetos", 5, 3.0)

print(biscoito, biscoito.total())
print(salgadinho, salgadinho.total())
print(salgadinho2, salgadinho2.total())

carrinho = Carrinho("Braulio", "26/11/2024")
carrinho.inserir(biscoito)
carrinho.inserir(salgadinho)
carrinho.inserir(salgadinho2)
print(carrinho)

for i in carrinho.listar():
    print(i)

print(carrinho.total())
