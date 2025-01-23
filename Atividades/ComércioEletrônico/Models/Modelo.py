from abc import ABC, abstractmethod

class Modelo(ABC):
    objetos = []

    @classmethod
    def inserir(cls, obj : object):
        cls.abrir()
        id = 0
        for objeto in cls.objetos:
            if objeto.getId():
                id = objeto.getId()
        obj.setId(id+1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    @abstractmethod
    def salvar(cls):
        pass

    @classmethod
    @abstractmethod
    def abrir(cls):
        pass

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def listarId(cls, id : int):
        cls.abrir()
        for i in cls.objetos():
            if i.getId() == id:
                return i
        return None
    
    @classmethod
    @abstractmethod
    def atualizar(cls, obj : object):
        x = cls.listarId(obj.getId())
        if x != None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj : object):
        x = cls.listar_id(obj.getId())
        if x!= None:
            cls.objetos.remove(x)
            cls.salvar()
    
