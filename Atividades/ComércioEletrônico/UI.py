from Cliente import Cliente, Clientes # Importando as classes
from Categoria import Categoria, Categorias

class UI: # Interface
    def menu(): #Menu 
        print("\nBEM VINDO AO SEU COMÉRCIO ELETRÔNICO\nOPÇÕES:\n1- Novo cliente, 2- Listar Clientes, 3- Atualizar clientes\n4- Inserir categoria, 5- Listar categorias, 6- Atualizar categorias\n9- Encerrar")
        return int(input("Digite uma opção: "))
    
    def main(): #Principal
        op = 0
        while op != 9:
            op = UI.menu() # Indo pro menu
            if op == 1:
                UI.inserir_cliente() # Se for 1, crie um cliente
            if op == 2:
                UI.listar_clientes() # Se for 2, liste os clientes
            if op == 3:
                UI.atualizar_clientes() # Se for 3, atualize os clientes
            if op == 4:
                UI.inserir_categoria()
            if op == 5:
                UI.listar_categorias()
            if op == 6:
                UI.atualizar_categorias()

# FUNÇÕES PARA CLIENTES

    @staticmethod
    def inserir_cliente(): # Criando um cliente
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        fone = input("Digite o fone: ")
        cliente = Cliente(1, nome, email, fone) # Variável que recebe os atributos do novo cliente, instânciando na classe Cliente
        Clientes.inserir(cliente) # Inserindo a variável na lista de clientes com o método Inserir da classe Cliente

    @classmethod
    def listar_clientes(cls): # Listando os clientes
        clientes = Clientes.listar() # Criando uma variável que chama o método da classe Clientes para listar
        if len(clientes) == 0: # Se não houver clientes
            print("Nenhum cliente cadastrado")
        else:
            for cliente in clientes: # Caso haja, mostre quem são
                print(cliente)

    @classmethod
    def atualizar_clientes(cls): # Atualizando clientes
        UI.listar_clientes() # Listando os clientes
        id = int(input("Digite o ip do cliente a ser alterado id: "))
        nome = input("Digite o novo nome: ")
        email = input("Digite o novo email: ")
        fone = input("Digite o novo fone: ")
        cliente = Cliente(id, nome, email, fone)
        Clientes.atualizar(cliente) # Usando o método atualizar na variável cliente

    @staticmethod
    def excluir_clientes():
        UI.listar_clientes()
        id = int(input("Informa o id do cliente a ser excluído: "))
        Clientes.excluir(Clientes.listar_id(id))

# FUNÇÕES PARA CATEGORIA

    @classmethod
    def inserir_categoria(cls):
        Descrição = input("Digite a descrição da categoria: ")
        ct = Categoria(1, Descrição)
        Categorias.inserir(ct)
    
    @classmethod
    def listar_categorias(cls):
        categorias = Categorias.listar()
        if len(categorias) == 0:
            print("Nenhuma categoria cadastrada")
        else:
            for categoria in categorias:
                print(categoria)
    
    @classmethod
    def atualizar_categorias(cls):
        UI.listar_categorias
        id = int(input("Digite o id da categoria a ser alterada: "))
        Descrição = input("Digite a nova descrição: ")
        categoria = Categoria(id, Descrição)
        Categorias.atualizar(categoria)


UI.main() # Executando a interface