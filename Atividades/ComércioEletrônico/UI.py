from View import View

class UI: # Interface
        
    # Dados do usuário logado
    cliente_id = 0
    cliente_nome = ""

    @staticmethod
    def menu(): #Menu 
        print("BEM VINDO AO COMÉRCIO ELETRÔNICO")
        print("Digite uma das opções:\n")
        print("Cadastro de Clientes:")
        print("1- Novo cliente, 2- Listar clientes, 3- Atualizar cliente, 4- Excluir Cliente")
        print("-----------------------------------------------------------------")
        print("Cadastro de Categorias:")
        print("5- Nova categoria, 6- Listar categorias, 7- Atualizar categoria, 8- Excluir categoria")
        print("-----------------------------------------------------------------")
        print("Cadastro de Produtos:")
        print("9- Novo produto, 10- Listar produtos, 11- Atualizar produto, 12- Excluir produto, 13- Produto reajustar")
        print("-----------------------------------------------------------------")
        print("Cadastro de Vendas:")
        print("14- Inserir no carrinho")
        print("Menu do visitante:")
        print("x- Criar conta, x- Entrar no sistema")
        print("-----------------------------------------------------------------")
        return int(input("Digite uma opção ou 20 para sair: "))
    
    @staticmethod
    def main(): #Principal
        View.cliente_admin()
        op = 0
        while op != 20:
            op = UI.menu() # Indo pro menu
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


            if op == 14:
                UI.inserir_carrinho()


            if op == "x":
                UI.visitante_abrir_conta()
            if op== "x":
                UI.cliente_entrar_sistema()


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
            cls.nome = obj["nome"]
            print(print("Bem-vindo(a),",cls.cliente_nome))


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




    @classmethod
    def inserir_carrinho(cls):
        UI.listar_produtos()
        produto = int(input("Informe o id do produto"))
        cliente = ""
        p = Venda(produto, )

UI.main() # Executando a interface