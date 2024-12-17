import json

class VendaItem:
    def __init__(self, id, qtd, preço, idVenda, idProduto):
        self.__id = id
        self.__qtd = qtd
        self.__preço = preço
        self.__idVenda = idVenda
        self.__idProduto = idProduto


    def getId(self):
        return self.__id
    def setId(self, id):
        if len(str(id)) > 0:
            self.__id = id
        else:
            raise ValueError('Id inválido')

    def getQtd(self):
        return self.__qtd
    def setQtd(self, qtd):
        if qtd < 0 :
            raise ValueError("Quantidade inválida")
        else: self.__qtd = qtd
    
    def getPreço(self):
        return self.__preço
    def setPreço(self, preço):
        if preço < 0:
            raise ValueError("Preço inválido")
        else: self.__preço = preço
    
    def getIdVenda(self):
        return self.__idVenda
    def setIdVenda(self, idVenda):
        self.__idVenda = idVenda
    
    def getIdProduto(self):
        return self.__idProduto
    def setIdProduto(self, idProduto):
        self.__idProduto = idProduto