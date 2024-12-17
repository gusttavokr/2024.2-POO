from datetime import datetime
import json

class Venda:
    def __init__(self, id, data, carrinho, total, id_cliente):
        self.__id = id
        self.__data = data
        self.__carrinho = carrinho
        self.__total = total
        self.__id_cliente = id_cliente
        
        if id<=0:
            raise ValueError("Id inválido")
        
        
    def getId(self):
        return self.__id
    def setId(self, id):
        self.__id = id
        
    def getData(self):
        return self.__data
    def setData(self, data = None):
        if data == None:
            self.__data = datetime.today()
        else:
            self.__data = data

    def getCarrinho(self):
        return self.__carrinho
    def setCarrinho(self):
        self.__carrinho = False

    def getTotal(self):
        return self.__total
    def setTotal(self):
        self.__total = 0.0
    
    def getIdCliente(self):
        return self.__id_cliente
    def setIdCliente(self, id_cliente):
        self.__id_cliente = id_cliente
    
    def __str__(self):
        return f"Id - {self.getId()}"
    
class Vendas:
    carrinho = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for i in cls.carrinho:
            if i.getId() > id:
                id = i.getId()
        obj.setId(id+1)
        cls.carrinho.append(obj)
        cls.salvar()

    @classmethod
    def abrir(cls):
        cls.carrinho=[]
        try:
            with open("Atividades/ComércioEletrônico/Json/Venda.json", mode="r") as arquivo:
                carrinho_obj = json.load(arquivo)
                for obj in carrinho_obj:
                    v = Venda(obj["_Venda__id"], datetime.strptime(obj["_Venda__data"]), obj["_Venda__carrinho"], obj["_Venda__total"], obj["_Venda__id_cliente"])
                    cls.carrinho.append(v)
        except FileNotFoundError:
            pass
    
    @classmethod
    def salvar(cls):
        with open('Atividades/ComércioEletrônico/Json/Venda.json', mode="w") as arquivo:
            json.dump(cls.carrinho, arquivo, default=vars) 
        
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.carrinho

    @classmethod
    def listar_id(cls, id):
        for x in cls.carrinho:
            if x.getId() == id:
                return x
        return None

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.getId())
        if x != None:
            cls.carrinho.remove(x)
            cls.carrinho.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.getId())
        if x != None:
            cls.carrinho.remove(x)
            cls.salvar()