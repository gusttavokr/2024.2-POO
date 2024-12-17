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

    def __str__(self):
        return f"{self.__id} - {self.__qtd} - {self.__preço}"


class VendaItens:
    itens = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for i in cls.itens:
            if i.getId() > id:
                id = i.getId()
        obj.setId(id+1)
        cls.itens.append(obj)
        cls.salvar()
    
    @classmethod
    def abrir(cls):
        cls.itens = []
        try:
            with open ("Atividades/ComércioEletrônico/Json/itens.json", mode="r") as arquivo:
                itens_obj = json.load(arquivo)
                for i in itens_obj:
                    it = VendaItem(i["_VendaItem__id"], i["_VendaItem__qtd"], i["_VendaItem__preço"], i["_VendaItem__idVenda"], i["_VendaItem__idProduto"])
                    cls.itens.append(it)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open ("Atividades/ComércioEletrônico/Json/itens.json", mode="r") as arquivo:
            json.dump(cls.itens, arquivo, default=vars)

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.itens
    
    @classmethod
    def listar_id(cls, id):
        for x in cls.itens:
            if x.getId() == id:
                return x
        return None
    
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.getId())
        if x != None:
            cls.itens.remove(x)
            cls.itens.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.getId())
        if x != None:
            cls.itens.remove(x)
            cls.salvar()