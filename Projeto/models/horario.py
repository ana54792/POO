from datetime import datetime

class Horario:
    def __init__(self, id, data, conf, id_c, id_s):
        self.set_id(id)
        self.set_data(data)
        self.set_confirmado(conf)
        self.set_id_cliente(id_c)
        self.set_id_servico(id_s)
    
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_data(self, data):
        if data < datetime.now(): raise ValueError("Data deve ser no futuro")
        self.__data = data
    def set_confirmado(self, conf):
        if conf == False: raise ValueError("Confirmação não foi feita")
        self.__confirmado = conf
    def set_id_cliente(self, id_c):
        if id_c < 0: raise ValueError("Id deve ser positivo")
        self.__id_cliente = id_c
    def set_id_servico(self, id_s):
        if id_s < 0: raise ValueError("Id deve ser positivo")
        self.__id_servico = id_s
        
                

    def get_id(self) : return self.__id
    def get_data(self) : return self.__data
    def get_confirmado(self) : return self.__confirmado
    def get_id_cliente(self) : return self.__id_cliente
    def get_id_servico(self) : return self.__id_servico

    def __str__(self):
        return f"{self.__id} - {datetime.strftime(self.__data, "%d/%m/%Y, %H:%M")} - {self.__confirmado} - {self.__id_cliente} - {self.__id_servico}"
    
    def to_json(self):
        return { "id":self.__id, "data": datetime.strftime(self.__data, "%d/%m/%Y, %H:%M"), "confirmado":self.__confirmado, "id_cliente":self.__id_cliente, "id_servico":self.__id_servico }
    
    @staticmethod
    def from_json(dic):
        return Horario(dic["id"], dic["data"], dic["confirmado"], dic["id_cliente"], dic["id_servico"])