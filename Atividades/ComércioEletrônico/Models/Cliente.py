import json
from Models.Modelo import Modelo

class Cliente:
    def __init__(self, id, nome, email, fone, senha): # Método construtor
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
        self.__senha = senha #fazer get e set
        
    def getId(self):
        return self.__id
    def setId(self, id):
        if len(str(id)) > 0:
            self.__id = id
        else:
            raise ValueError('Id inválido')

    def getNome(self):
        return self.__nome
    def setNome(self, nome):
        if len(nome) > 0:
            self.__nome = nome
        else:
            raise ValueError('Nome inválido')

    def getEmail(self):
        return self.__email
    def setEmail(self, email):
        if len(email) > 0:
            self.__email = email
        else:
            raise ValueError('Email inválido')

    def getFone(self):
        return self.__fone
    def setFone(self, fone):
        if len(fone) > 0:
            self.__fone = fone
        else:
            raise ValueError('Fone inválido')

    def getSenha(self):
        return self.__senha
    def setSenha(self, senha):
        if len(senha) > 0:
            self.__senha = senha
        else:
            raise ValueError('Senha inválida')

    def __str__(self): # Formatação do terminal
        return f'{self.getId()} - Nome: {self.getNome()} - Email: {self.getEmail()} - Telefone: {self.getFone()}'
    
class Clientes(Modelo):
    @classmethod
    def salvar(cls): 
        # Mesma coisa do abrir, porém ele escreve por cima
        # open - cria e abre um arquivo.json
        # dump - para subir as informações pro arquivo json
        # vars - para organizar em dicionário no arquivo
        with open ("Atividades/ComércioEletrônico/Json/clientela.json", mode="w") as arquivo: 
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos=[]
        try: # Ele tentará ler/criar um arquivo.json no modo leitura
            with open ("Atividades/ComércioEletrônico/Json/clientela.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo) # Criando uma variável para carregar o arquivo
                for obj in objetos_json: # Iterando os atributos da variável
                    c = Cliente(obj["_Cliente__id"], obj["_Cliente__nome"],obj["_Cliente__email"],obj["_Cliente__fone"], obj["_Cliente__senha"]) # Instanciando os atributos da classe Cliente à uma variável
                    cls.objetos.append(c) # Adicionando a variável na lista dos objetos
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass