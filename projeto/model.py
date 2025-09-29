class Item:
    def __init__(self, nome, descricao, quantidade, id = None):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.set_quantidade(quantidade)

    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id

    def set_descricao(self, descricao):
        if descricao == "": raise ValueError("A descrição não pode ser vazia.")
        self.__descricao = descricao
    def get_descricao(self):
        return self.__descricao
        
    def set_nome(self, nome):
        if nome == "": raise ValueError("O nome não pode ser vazio.")
        self.__nome = nome
    def get_nome(self):
        return self.__nome

    def set_quantidade(self, quantidade):
        if quantidade < 0: raise ValueError("A quantidade não pode ser um número negativo.")
        self.__quantidade = quantidade
    def get_quantidade(self):
        return self.__quantidade
    
    def __str__(self):
        return f"{self.get_id()} - Nome: {self.get_nome()} | Descrição: {self.get_descricao()} | Quantidade: {self.get_quantidade()}"