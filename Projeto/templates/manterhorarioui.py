import streamlit as st
import pandas as pd
import time
from service import Service
from datetime import datetime
from models.cliente import Cliente
from models.servico import Servico

class ManterHorarioUI:
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()
    def listar():
        horarios = Service.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horario cadastrado")
        else:
            list_dic = []
            for obj in horarios: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        data = st.text_input("Informe a data (dd/mm/aaaa, hh:mm)")
        
        # id_cliente = Cliente.get_id
        # id_servico = Servico.get_id
        if st.button("Avançar", key="avancar"):
            
        if st.button("Cadastrar", key="cadastro_horario"):
            data = datetime.strptime(data, "%d/%m/%Y, %H:%M")
            Service.horario_inserir(data)
            st.success("Horário inserido com sucesso")
            time.sleep(2)
            st.rerun()
    def atualizar():
        horarios = Service.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Atualização de Horários", horarios)
            data = st.text_input("Novo data", op.get_data())
            
            
            if st.button("Atualizar", key="atualizar_horario"):
                id = op.get_id()
                # id_cliente = op.get_id_cliente()
                # id_servico = op.get_id_servico()
                Service.horario_atualizar(id, data)
                st.success("Horário atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    def excluir():
        horarios = Service.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Exclusão de Horários", horarios)
            if st.button("Excluir", key="excluir_horario"):
                id = op.get_id()
                Service.horario_excluir(id)
                st.success("Horário excluído com sucesso")
                time.sleep(2)
                st.rerun()