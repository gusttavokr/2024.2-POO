import json

class Cliente:
    def __init__(self, id, nome, email, fone): # Método construtor
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone

    # def getId(self):
    #     return self.__id
    # def setId(self, id):
    #     if len(id) > 0:
    #         self.__id = id
    #     else:
    #         raise ValueError('Id inválido')

    # def getNome(self):
    #     return self.__nome
    # def setNome(self, nome):
    #     if len(nome) > 0:
    #         self.__nome = nome
    #     else:
    #         raise ValueError('Nome inválido')

    # def getEmail(self):
    #     return self.__email
    # def setEmail(self, email):
    #     if len(email) > 0:
    #         self.__email = email
    #     else:
    #         raise ValueError('Email inválido')

    # def getFone(self):
    #     return self.__fone
    # def setFone(self, fone):
    #     if len(fone) > 0:
    #         self.__fone = fone
    #     else:
    #         raise ValueError('Fone inválido')

    def __str__(self):
        return f'{self.id} - {self.nome} - {self.email} - {self.fone}'
    
class Clientes:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for x in cls.objetos:
            if x.id > id:
                id = x.id
        obj.id = id +1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def salvar(cls):
        with open ("Atividades/ComércioEletrônico/clientela.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos=[]
        try:
            with open ("Atividades/ComércioEletrônico/clientela.json", mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Cliente(obj["id"], obj["nome"],obj["email"],obj["fone"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        for x in cls.objetos:
            if x.id == id:
                return x
        return None

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            x.nome = obj.nome
            x.email = obj.email
            x.fone = obj.fone
            cls.salvar()