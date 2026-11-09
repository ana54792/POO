from models.horario import Horario
from models.dao import DAO
import json

class HorarioDAO(DAO):
    def __init__(self):
        super().__init__("clientes.json")

    def __abrir(self):  
        try:  
            arquivo = open(self.__arquivo, mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            self.__objetos = []
            for dic in list_dic:
                obj = Horario.from_json(dic)
                self.__objetos.append(obj)
        except FileNotFoundError:
            pass

    def __salvar(self):    
        arquivo = open(self.__arquivo, mode = "w")
        json.dump(self.__objetos, arquivo, default = Horario.to_json, indent = 2)
        arquivo.close()
        