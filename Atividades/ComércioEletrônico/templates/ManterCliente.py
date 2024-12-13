import streamlit as st
import pandas as p
from View import View
import time

class ManterCliente:
    def main():
        st.header("Cadastro de clientes")
        1, 2, 3, 4 = st.tabs(["Inserir"], ["Listar"], ["Atualizar"], ["Excluir"])
        with 1 : ManterCliente.inserir()
        with 2 : ManterCliente.listar()

    def inserir():
        nome = st.text_input("Informe o nome do cliente:")
        email = st.text_input("Informe o email do cliente:")
        fone = st.text_input("Informe o telefone do usuário:")
        senha = st.text_input("Informe a senha do usuário:", type="password")

        if st.button("Enviar"):
            View.inserir_cliente(nome, email, fone, senha)
            st.sucess("Cliente inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def listar():
        clientes = View.listar_clientes()

        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            dic = []
            for obj in clientes:
                dic.append(obj.__dict__)
                df = p.DataFrame(dic)
                st.dataframe(df)

    def atualizar():
        clientes = View.listar_clientes()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Atualização de cliente", clientes)
            nome = st.text_input("Informe o novo nome:", op.nome)
            email = st.text_input("Informe o novo email:", op.email)
            fone = st.text_input("Informe o novo telefone:", op.fone)
            senha = st.text_input("Informe o novo senha:", op.senha)
        
        if st.button("Atualizar"):
            View.atualizar_clientes(op.id, nome, email, fone, senha)
            st.sucess("Cliente atualizado com sucesso!")
            time.sleep(2)
            st.rerun()

    def excluir():
        clientes = View.listar_clientes()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Excluir cliente", clientes)
            if st.button("Excluir"):
                View.excluir_clientes(op.id)
                st.sucess("Cliente excluído com sucesso")
                time.sleep(2)
                st.rerun()