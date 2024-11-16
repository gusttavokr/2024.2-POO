import json

class Categoria:
    def __init__(self, id, descrição): # Método construtor
        self.__id = id # Atribuindo como privado
        self.__descrição = descrição

    def getId(self):
        return self.__id
    def setId(self, id):
        if len(str(id))>0:
            self.__id = id
        else:
            raise ValueError('Id inválido')

    def getDesc(self):
        return self.__descrição
    def setDesc(self, descrição):
        if len(descrição) > 0:
            self.__descrição = descrição
        else:
            raise ValueError('Descrição inválida')
        
    def __str__(self):
        return f'{self.getId()} - {self.getDesc()}'

class Categorias:
    categorias = []

    @classmethod
    def abrirCat(cls):
        cls.categorias = []
        try:
            with open('Atividades/ComércioEletrônico/categorias.json', mode='r') as arquivo:
                categorias_json = json.load(arquivo)
                for obj in categorias_json:
                    ct = Categoria(obj["_Categoria__id"], obj["_Categoria__descrição"])
                    cls.categorias.append(ct)
        except FileNotFoundError:
            pass

    @classmethod
    def salvarCat(cls):
        with open('Atividades/ComércioEletrônico/categorias.json', mode='w') as arquivo:
            json.dump(cls.categorias, arquivo, default=vars)

    @classmethod
    def inserir(cls, obj):
        cls.abrirCat()
        id = 0
        for x in cls.categorias:
            if x.getId() > id:
                id = x.getId()
        obj.setId(id+1)
        cls.categorias.append(obj)
        cls.salvarCat()

    @classmethod
    def listar(cls):
        cls.abrirCat()
        return cls.categorias
    
    @classmethod
    def listar_id(cls, id):
        for x in cls.categorias:
            if x.getId() == id:
                return x
        return None

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.getId())
        if x != None:
            x.setDesc(obj.getDesc())
            cls.salvarCat()
