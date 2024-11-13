import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"

class Clientes:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for x in cls.objetos:
            if x.id > id:
                id = x.id
        obj.id = id + 1
        cls.objetos.append(obj)
        cls.salvar()

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
        #obj é o objeto que tem o id a ser encontrado e os novos dados
       
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()

    @classmethod
    def salvar(cls):
        # open - cria e abre um arquivo clientes.json
        # dump - 
        # vars - 

        with open ("Praticando/Aula10-Dicionário/Projeto/clientela.json", mode="w") as arquivo:
        # abra um arquivo (nome do arquivo), no modo de leitura para (variável)
            json.dump(cls.objetos, arquivo, default = vars)
            # passe clientes para a variável em dicionário

    @classmethod
    def abrir(cls):
        # esvazia a lista de objetos
        cls.objetos = []
        try:
            with open ("Praticando/Aula10-Dicionário/Projeto/clientela.json", mode="r") as arquivo:
            #abre o arquivo com a lista de dicionários
                clientes_json = json.load(arquivo)
                # percorre a lista de dicionários
                for obj in clientes_json:
                    # recupera cada dicionário e cria um objeto
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                    # insere o objeto na lista
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass