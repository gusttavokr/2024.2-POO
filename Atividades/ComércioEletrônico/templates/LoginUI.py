from View import View
import streamlit as st

class LoginUI:
    def main():
        st.header("Entrar no sistema")
        email = st.text_input("Digite o email:")
        senha = st.text_input("Digite a senha:", type="password")
        if st.button("Entrar"):
            c = View.cliente_autenticar(email, senha)
            if c == None:
                st.write("Email ou senha inválidos")
            else:
                st.session_state["cliente_id"] = c["id"]
                st.session_state["cliente_nome"] = c["nome"]
                st.rerun()