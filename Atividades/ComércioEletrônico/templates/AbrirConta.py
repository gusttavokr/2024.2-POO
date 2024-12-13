import streamlit as st
from View import View
import time

class AbrirConta:
    def main():
        st.header("Abrir conta no sistema")
        AbrirConta.inserir()


    def inserir():
        nome = st.text_input("Informe o nome do cliente:")
        email = st.text_input("Informe o email do cliente:")
        fone = st.text_input("Informe o telefone do usuário:")
        senha = st.text_input("Informe a senha do usuário:", type="password")

        if st.button("Cadastrar"):
            View.inserir_cliente(nome, email, fone, senha)
            st.success("Cliente inserido com sucesso")
            time.sleep(2)
            st.rerun()