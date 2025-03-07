import json
from Models.Modelo import Modelo

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

class Categorias(Modelo):

    @classmethod
    def abrirCat(cls):
        cls.categorias = []
        try:
            with open('Atividades/ComércioEletrônico/Json/categorias.json', mode='r') as arquivo:
                categorias_json = json.load(arquivo)
                for obj in categorias_json:
                    ct = Categoria(obj["_Categoria__id"], obj["_Categoria__descrição"])
                    cls.categorias.append(ct)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass

    @classmethod
    def salvarCat(cls):
        with open('Atividades/ComércioEletrônico/Json/categorias.json', mode='w') as arquivo:
            json.dump(cls.categorias, arquivo, default=vars)