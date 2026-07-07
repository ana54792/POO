from Models.Cliente import Cliente
from Models.ClienteDAO import ClienteDAO
from Models.Servico import Serviço
from Models.ServicoDAO import ServiçoDAO

class Service:
    @staticmethod
    def cliente_inserir(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        ClienteDAO().inserir(obj)
    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(obj)
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)
    @staticmethod
    def servico_inserir(id, descricao, valor):
        objt = Serviço(id, descricao, valor)
        ServiçoDAO().inserir(objt)
    @staticmethod
    def servico_listar():
        return ServiçoDAO().listar()
    @staticmethod
    def servico_listar_id(id):
        return ServiçoDAO().listar_id(id)
    @staticmethod
    def servico_atualizar(id, descricao, valor):
        objt = Serviço(id, descricao, valor)
        ServiçoDAO().atualizar(objt)
    @staticmethod
    def servico_excluir(id):
        ServiçoDAO().excluir(id)
    