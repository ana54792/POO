from service import Service

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.servico_inserir()
            if op == 6: UI.servico_listar()
            if op == 7: UI.servico_atualizar()
            if op == 8: UI.servico_excluir()

    @staticmethod
    def menu():
        print("1-Inserir cliente, 2-Listar cliente, 3-Atualizar cliente, 4-Excluir cliente, 5-Inserir serviço, 6-Listar serviço, 7-Atualizar serviço, 8-Excluir serviço, 9-Fim")
        return int(input("Informe uma opção: "))

    @classmethod
    def cliente_inserir():
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        Service.cliente_inserir(id, nome, email, fone)

    @classmethod
    def cliente_listar(obj):
        for obj in Service.cliente_listar(): print(obj)

    @classmethod
    def cliente_atualizar(obj):
        for obj in Service().cliente_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo telefone: ")
        Service.cliente_atualizar(id, nome, email, fone)

    @classmethod
    def cliente_excluir(obj):
        for obj in Service().cliente_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser excluído: "))
        Service.cliente_excluir(id)


    @classmethod
    def servico_inserir():
        id = int(input("Informe o id: "))
        descricao = input("Informe o descrição: ")
        valor = float(input("Informe o valor: "))
        
        Service.servico_inserir(id, descricao, valor)

    @classmethod
    def servico_listar(obj):
        for obj in Service.servico_listar(): print(obj)

    @classmethod
    def servico_atualizar(obj):
        for obj in Service().servico_listar(): print(obj)
        id = int(input("Informe o id do serviço a ser atualizado: "))
        
        descricao = input("Informe o novo descrição: ")
        valor = float(input("Informe o novo valor: "))
        
        Service.servico_atualizar(id, descricao, valor)

    @classmethod
    def servico_excluir(obj):
        for obj in Service().servico_listar(): print(obj)
        id = int(input("Informe o id do serviço a ser excluído: "))
        Service.servico_excluir(id)

UI.main()