import streamlit as st
from EquaçãoUI import EquaçãoUI
from retanguloUI import RetanguloUI

op = st.sidebar.selectbox("Menu", ["Retângulo", "Equação"])
if op == "Retângulo":
    RetanguloUI.main()
if op == "Equação":
    EquaçãoUI.main()