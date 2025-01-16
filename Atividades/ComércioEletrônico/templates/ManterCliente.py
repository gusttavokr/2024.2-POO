import streamlit as st
import pandas as p
from View import View
import time

class ManterCliente:
    def main():
        st.header("Cadastro de Clientes")
        t1, t2, t3, t4 = st.tabs(["Inserir", "Listar", "Atualizar", "Excluir"])
        with t1 : ManterCliente.inserir()
        with t2 : ManterCliente.listar()
        with t3 : ManterCliente.atualizar()
        with t4 : ManterCliente.excluir()

    def inserir():
        nome = st.text_input("Informe o nome do cliente:")
        email = st.text_input("Informe o email do cliente:")
        fone = st.text_input("Informe o telefone do usuário:")
        senha = st.text_input("Informe a senha do usuário:", type="password")

        if st.button("Cadastrar"):
            try:
                View.inserir_cliente(nome, email, fone, senha)
                st.success("Cliente inserido com sucesso")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)

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
            nome = st.text_input("Informe o novo nome:", op.getNome())
            email = st.text_input("Informe o novo email:", op.getEmail())
            fone = st.text_input("Informe o novo telefone:", op.getFone())
            senha = st.text_input("Informe o novo senha:", op.getSenha())
        
        if st.button("Atualizar"):
            View.atualizar_clientes(op.getId(), nome, email, fone, senha)
            st.success("Cliente atualizado com sucesso!")
            time.sleep(2)
            st.rerun()

    def excluir():
        clientes = View.listar_clientes()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Excluir cliente", clientes)
            print(op)
            if st.button("Excluir"):
                View.excluir_clientes(op.getId())
                st.success("Cliente excluído com sucesso")
                time.sleep(2)
                st.rerun()