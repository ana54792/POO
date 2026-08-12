from paciente import Paciente
import streamlit as st
from datetime import datetime

class PacienteUI:
    def main():
        st.header("Cálculo de Idade")
        n = st.text_input("Informe o nome")
        c = st.text_input("Informe o CPF")
        t = st.text_input("Informe o telefone")
        nasc = st.text_input("Informe a data de nascimento (dd/mm/aaaa)")
        
        if st.button("Calcular"):
            nasc = datetime.strptime(nasc, "%d/%m/%Y")
            p = Paciente(n, c, t, nasc)
            st.write(f"Idade = {p.idade(nasc)}")
            st.write(p)          