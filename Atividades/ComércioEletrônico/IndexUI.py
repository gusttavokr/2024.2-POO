import streamlit as st
from templates.LoginUI import LoginUI
from templates.ManterCliente import ManterCliente
from templates.ManterCategoria import ManterCategoria
#from templates.ManterProduto import ManterProduto
from templates.AbrirConta import AbrirConta
from View import View

class IndexUI:
    def menu_visitante():
        op = st.selectbox("Menu", ["Criar conta", "Entrar no sistema"])
        if op == "Criar conta":
            AbrirConta.main()
        if op == "Entrar no sistema":
            LoginUI.main()

    def menu_admin():
        op = st.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Categorias", "Cadastro de Produtos"])
        if op == "Cadastro de Clientes":
            ManterCliente.main()
        if op == "Cadastro de Categorias":
            ManterCategoria.main()
        # if op == "Cadastro de Produtos":
        #     ManterProduto.main()

    def menu_cliente():
        op = st.selectbox("Menu", ["Inserir produtos ao carrinho", "Listar produtos", "Fechar pedido", "Ver meus pedidos"])

    def sair():
        if st.button("Sair"):
            del st.session_state["cliente_id"]
            del st.session_state["cliente_nome"]
            st.rerun()

    def sidebar():
        if "cliente_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["cliente_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
            if admin:
                IndexUI.menu_admin()
            else:
                IndexUI.menu_cliente()
            IndexUI.sair()

    def main():
        View.cliente_admin()

        IndexUI.sidebar()

IndexUI.main()