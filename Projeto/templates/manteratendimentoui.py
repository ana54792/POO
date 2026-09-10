import streamlit as st
import pandas as pd
from service import Service
import time
from datetime import datetime

class ManterAtendimentoUI:
    def main():
        st.header("Cadastro de Atendimentos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterAtendimentoUI.listar()
        with tab2: ManterAtendimentoUI.inserir()
        with tab3: ManterAtendimentoUI.atualizar()
        with tab4: ManterAtendimentoUI.excluir()

    def listar():
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0: st.write("Nenhum atendimento cadastrado")
        else:
            dic = []
            for obj in atendimentos:
                horario = Service.horario_listar_id(obj.get_id())
                if horario != None: 
                    id_cliente = horario.get_id_cliente()
                    cliente = Service.cliente_listar_id(id_cliente)
                    nome = cliente.get_nome()
                
                dic.append({"id" : obj.get_id(), "data" : obj.get_data(), "queixa_principal" : obj.get_queixa_principal(), "historico_saude" : obj.get_historico_saude(), "avaliacao" : obj.get_avaliacao(), "prescricao" : obj.get_prescricao(), "nome" : nome})
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        horarios = Service.horario_listar()
        data = st.text_input("Informe a data e atendimento do serviço", datetime.now().strftime("%d/%m/%Y %H:%M"))
        queixa_principal = st.text_input("Informe a queixa principal do paciente: ")
        historico_saude = st.text_input("Informe o histórico de saúde do paciente: ")
        avaliacao = st.text_input("Informe a avalição do paciente: ")
        prescricao = st.text_input("Informe a prescrição do paciente: ")
        
        horario = st.selectbox("Informe o atendimento", horarios, index = None)
        
        if st.button("Inserir"):
            id_horario = None
            
            if horario != None: id_horario = horario.get_id()
            
            Service.atendimento_inserir(datetime.strptime(data, "%d/%m/%Y %H:%M"), queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
            st.success("Atendimento inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0: st.write("Nenhum atendimento cadastrado")
        else:
            horarios = Service.horario_listar()
            op = st.selectbox("Atualização de Atendimentos", atendimentos)
            data = st.text_input("Informe a nova data e horario do atendimento", op.get_data().strftime("%d/%m/%Y %H:%M"))
            queixa_principal = st.text_input("Informe a queixa principal do paciente: ", op.get_queixa_principal())
            historico_saude = st.text_input("Informe o histórico de saúde do paciente: ", op.get_historico_saude())
            avaliacao = st.text_input("Informe a avalição do paciente: ", op.get_avaliacao())
            prescricao = st.text_input("Informe a prescrição do paciente: ", op.get_prescricao())
            id_horario = None if op.get_id_horario() in [0, None] else op.get_id_horario()
            
            horario = st.selectbox("Informe o novo horario", horarios, next((i for i, c in enumerate(horarios) if c.get_id() == id_horario), None))
            if st.button("Atualizar"):
                id_horario = None
                if horario != None: id_horario = horario.get_id()
                
                Service.atendimento_atualizar(op.get_id(), datetime.strptime(data, "%d/%m/%Y %H:%M"), queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
                st.success("Atendimento atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0: st.write("Nenhum atendimento cadastrado")
        else:
            op = st.selectbox("Exclusão de Atendimentos", atendimentos)
            if st.button("Excluir"):
                Service.atendimento_excluir(op.get_id())
                st.success("Atendimento excluído com sucesso")
                time.sleep(2)
                st.rerun()