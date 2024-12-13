from View import View

class UI: # Interface
        
    # Dados do usuário logado
    cliente_id = 0
    cliente_nome = ""

    @staticmethod
    def menu_visitante(): #Menu 
        print("1- Criar conta, 2- Entrar no sistema, 99- Fim")
        print("-----------------------------------------------------------------")
        op = int(input("\nDigite uma opção: "))
    
        if op == 1:
            UI.visitante_abrir_conta()
        if op== 2:
            UI.cliente_entrar_sistema()

    @staticmethod
    def menu_admin():
        print("Cadastro de Clientes:")
        print("1- Novo cliente, 2- Listar clientes, 3- Atualizar cliente, 4- Excluir Cliente")
        print("-----------------------------------------------------------------")
        print("Cadastro de Categorias:")
        print("5- Nova categoria, 6- Listar categorias, 7- Atualizar categoria, 8- Excluir categoria")
        print("-----------------------------------------------------------------")
        print("Cadastro de Produtos:")
        print("9- Novo produto, 10- Listar produtos, 11- Atualizar produto, 12- Excluir produto, 13- Produto reajustar")
        print("-----------------------------------------------------------------")
        print("0- Sair, 99 - Fim")

        op = int(input("Digite uma operação: "))

        if op == 0:
            UI.sair_do_sistema()

        if op == 1:
            UI.inserir_cliente() # Se for 1, crie um cliente
        if op == 2:
            UI.listar_clientes() # Se for 2, liste os clientes
        if op == 3:
            UI.atualizar_clientes() # Se for 3, atualize os clientes
        if op == 4:
            UI.excluir_clientes()

        if op == 5:
            UI.inserir_categoria()
        if op == 6:
            UI.listar_categorias()
        if op == 7:
            UI.atualizar_categorias()
        if op == 8:
            UI.excluir_categorias()

        if op == 9:
            UI.inserir_produto()
        if op == 10:
            UI.listar_produtos()
        if op == 11:
            UI.atualizar_produtos()
        if op == 12:
            UI.excluir_produtos()
        if op == 13:
            UI.produto_reajustar()

        return op
    
    def menu_cliente():
        print("1 - Listar Produtos, 2- Adicionar Produto no Carrinho, 3- Fechar Pedido, 4- Ver Meus Pedidos")
        print("0 - Sair, 99 - Fim")
        op = int(input("\nInforme uma opção: "))
        if op == 0: UI.sair_do_sistema()

        if op == 1: UI.cliente_listar_produto()
        if op == 2: UI.cliente_adicionar_produto()
        if op == 3: UI.cliente_fechar_pedido()
        if op == 4: UI.cliente_meus_pedidos()
        return op
    
    @classmethod
    def main(cls): #Principal
        View.cliente_admin()
        op = 0

        while op != 99:
            if cls.cliente_id == 0:
                op = UI.menu_visitante()
            else:
                admin = cls.cliente_nome == "admin"
                print("Bem-vindo(a), " + cls.cliente_nome)
                if admin:
                    op = UI.menu_admin()
                else: 
                    op = UI.menu_cliente()


    @classmethod
    def sair_do_sistema(cls):
        cls.cliente_id = 0
        cls.cliente_nome = ""

    @classmethod
    def visitante_abrir_conta(cls):
        cls.inserir_cliente()
    @classmethod
    def cliente_entrar_sistema(cls):
        email = input("Informe o email: ")
        senha = input("Informe a senha: ")
        obj = View.cliente_autenticar(email, senha)
        if obj == None:
            print("Email ou senha inválidos")
        else:
            cls.cliente_id = obj["id"]
            cls.cliente_nome = obj["nome"]

# FUNÇÕES PARA CLIENTES

    @staticmethod
    def inserir_cliente(): # Criando um cliente
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        fone = input("Digite o fone: ")
        senha = input("Digite a senha: ")
        View.inserir_cliente(nome, email, fone, senha)

    @classmethod
    def listar_clientes(cls): # Listando os clientes
        clientes = View.listar_clientes() # Criando uma variável que chama o método da classe Clientes para listar
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
        senha = input("Digite o nova senha: ")
        View.atualizar_clientes(id, nome, email, fone, senha)

    @staticmethod
    def excluir_clientes():
        UI.listar_clientes()
        id = int(input("Informa o id do cliente a ser excluído: "))
        View.excluir_clientes(id)

# FUNÇÕES PARA CATEGORIA

    @classmethod
    def inserir_categoria(cls):
        Descrição = input("Digite a descrição da categoria: ")
        View.inserir_categoria(Descrição)
    
    @classmethod
    def listar_categorias(cls):
        categorias = View.listar_categorias()
        if len(categorias) == 0:
            print("Nenhuma categoria cadastrada")
        else:
            for categoria in categorias:
                print(categoria)
    
    @classmethod
    def atualizar_categorias(cls):
        UI.listar_categorias()
        id = int(input("Digite o id da categoria a ser alterada: "))
        Descrição = input("Digite a nova descrição: ")
        View.atualizar_categorias(id, Descrição)
    
    @staticmethod
    def excluir_categorias():
        UI.listar_categorias()
        id = int(input("Digite o id da categoria que deseja excluir: "))
        View.excluir_categorias(id)

# FUNÇÕES PARA PRODUTOS

    @classmethod
    def inserir_produto(cls):
        Descrição = input("Digite a descrição do produto: ")
        Preço = float(input("Digite o preço do produto: "))
        Estoque = int(input("Digite o estoque do produto: "))
        UI.listar_categorias()
        id_categoria = int(input("Digite o id da categoria: "))
        View.inserir_produto(1, Descrição, Preço, Estoque, id_categoria)
    
    @classmethod
    def listar_produtos(cls):
        produtos = View.listar_produtos()
        if len(produtos) == 0:
            print("Nenhum produto cadastrado")
        else:
            for produto in produtos:
                print(produto)

    @classmethod
    def atualizar_produtos(cls):
        UI.listar_produtos()
        id = int(input("Digite o id do produto que deseja atualizar: "))
        descrição = input("Digite a nova descrição do produto: ")
        preço = float(input("Digite o novo preço do produto: "))
        estoque = int(input("Digite o estoque do novo produto: "))
        UI.listar_categorias()
        id_categoria = int(input("Digite o id da categoria do produto: "))
        View.atualizar_produtos(id, descrição, preço, estoque, id_categoria)

    @staticmethod
    def excluir_produtos():
        UI.listar_produtos()
        id = int(input("Digite o id a ser excluído: "))
        View.excluir_produtos(id)

    @classmethod
    def produto_reajustar(cls):
        reajuste = float(input("Informe o percentual de reajuste em %: "))
        View.produto_reajustar(reajuste/100)




    # @classmethod
    # def inserir_carrinho(cls):
    #     UI.listar_produtos()
    #     produto = int(input("Informe o id do produto"))
    #     cliente = ""
    #     p = Venda(produto, )

UI.main() # Executando a interface