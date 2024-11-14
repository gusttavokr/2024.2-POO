from Cliente import Cliente, Clientes # Importando as classes

class UI: # Interface
    def menu(): #Menu 
        print("1- Novo cliente, 2- Listar Clientes\n3- Atualizar clientes, 9- Fim")
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
                UI.atualizar_clientes() # Se for três, atualize os clientes

    @classmethod
    def inserir_cliente(cls): # Criando um cliente
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        fone = input("Digite o fone: ")
        cliente = Cliente(0, nome, email, fone) # Variável que recebe os atributos do novo cliente, instânciando na classe Cliente
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
        Clientes.atualizar(cliente)



UI.main()