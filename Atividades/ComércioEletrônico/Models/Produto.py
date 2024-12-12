import json

class Produto:
    def __init__(self, id, descrição, preço, estoque, id_categoria):
        self.__id = id
        self.__descrição = descrição
        self.__preço = preço
        self.__estoque = estoque
        self.__id_categoria = id_categoria

        if id<=0:
            raise ValueError("Id inválido")
        if descrição == "":
            raise ValueError("Descrição inválida")
        if preço <= 0:
            raise ValueError("Preço inválido")
        if estoque < 0:
            raise ValueError("Estoque inválido")
        
    def getId(self):
        return self.__id
    def setId(self, id):
        if len(str(id)) > 0:
            self.__id = id
        else: raise ValueError("Id inválido")
        
    def getDesc(self):
        return self.__descrição
    def setDesc(self, descrição):
        self.__descrição = descrição
        if descrição == "":
            raise ValueError("Descrição inválida")
    
    def getPreço(self):
        return self.__preço
    def setPreço(self, preço):
        self.__preço = preço
        if preço <= 0:
            raise ValueError("Preço inválido")
        
    def getEstoque(self):
        return self.__estoque
    def setEstoque(self, estoque):
        self.__estoque = estoque
        if estoque < 0:
            raise ValueError("Estoque inválido")

    def getId_Categoria(self):
        return self.__id_categoria
    def setId_Categoria(self, id_categoria):
        self.__id_categoria = id_categoria
        
    def __str__(self):
        return f"{self.getId()} - Produto: {self.getDesc()} - R${self.getPreço():.2f} - {self.getEstoque()} unidades"
    
class Produtos:
    produtos = []

    @classmethod
    def abrirProd(cls):
        cls.produtos = []
        try:
            with open("Atividades/ComércioEletrônico/Json/produtos.json", mode="r") as arquivo:
                produtos_json=json.load(arquivo)
                for obj in produtos_json:
                    p = Produto(obj["_Produto__id"], obj["_Produto__descrição"], obj["_Produto__preço"], obj["_Produto__estoque"], obj["_Produto__id_categoria"])
                    #p.id_categoria = obj["__id_categoria"]
                    cls.produtos.append(p)
        except FileNotFoundError:
            pass
    
    @classmethod
    def inserir(cls, obj):
        cls.abrirProd()
        id = 0
        for i in cls.produtos:
            if i.getId() > id:
                id = i.getId()
        obj.setId(id+1)
        cls.produtos.append(obj)
        cls.salvarProd()

    @classmethod
    def salvarProd(cls):
        with open('Atividades/ComércioEletrônico/Json/produtos.json', mode="w") as arquivo:
            json.dump(cls.produtos, arquivo, default=vars)

    @classmethod
    def listarProd(cls):
        cls.abrirProd()
        return cls.produtos
    
    @classmethod
    def listarId(cls, id):
        for x in cls.produtos:
            if x.getId() == id:
                return x
        return None

    @classmethod
    def atualizarProd(cls, obj):
        x = cls.listarId(obj.getId())
        if x != None:
            cls.produtos.remove(x)
            cls.produtos.append(obj)
            #x.setDesc(obj.getDesc())
            #x.setPreço(obj.getPreço())
            #x.setEstoque(obj.getEstoque())
            cls.salvarProd()

    @classmethod
    def excluir(cls, obj):
        x = cls.listarId(obj.getId())
        if x != None:
            cls.produtos.remove(x)
            cls.salvarProd()