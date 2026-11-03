import streamlit as st
import pandas as pd
from service import Service

class ListarAgendaProfissionalUI:
    def main():
        st.header("Agenda Profissional")
        horarios = Service.horario_listar_agenda_profissional('id', 'data', 'id_servico', 'id_cliente', 'id_profissional')
        if st.button("Visualizar"):
            if len(horarios) == 0: st.write("Nenhum horário encontrado na agenda")
            else:
                dic = []
                for obj in horarios:
                    cliente = Service.cliente_listar_id(obj.get_id_cliente())
                    servico = Service.servico_listar_id(obj.get_id_servico())
                    profissional = Service.profissional_listar_id(obj.get_id_profissional())
                    
                    if cliente != None: cliente = cliente.get_nome()
                    if servico != None: servico = servico.get_descricao()
                    if profissional != None: profissional = profissional.get_nome()
                    dic.append({"id" : obj.get_id(), "data" : obj.get_data(),
                    "confirmado" : obj.get_confirmado(), "cliente" : cliente,
                    "serviço" : servico, "profissional" : profissional})
                df = pd.DataFrame(dic) 
                st.dataframe(df)