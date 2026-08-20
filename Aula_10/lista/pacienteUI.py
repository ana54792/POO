from paciente import Paciente
import streamlit as st
from datetime import datetime

class PacienteUI:
    def main():
        st.header("Dados do paciente")
        n = st.text_input("Informe o nome")
        c = st.text_input("Informe o CPF")
        t = st.text_input("Informe o telefone")
        nasc = st.text_input("Informe a data de nascimento (dd/mm/aaaa)")
        #nasc = st.date_imput("Data de nascimento", value = date(2000,1,1), min_value = date(1900, 1, 1), max_value = date.today(), format = "DD/MM/YYYY")
        #nasc = datetime.combine(nasc, datetime.min.time())
        if st.button("Calcular"):
            nasc = datetime.strptime(nasc, "%d/%m/%Y")
            p = Paciente(n, c, t, nasc)
            st.write(f"Idade = {p.idade(nasc)}")
            st.write(p)          