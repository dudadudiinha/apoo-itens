from dao import ItemDAO
from model import Item

class ItemController:
    def __init__(self):
        self.dao = ItemDAO()

    def criarItem(self, nome: str, descricao: str, quantidade: int):
        item = Item(nome=nome, descricao=descricao, quantidade=quantidade)
        self.dao.adicionar(item)

    def obterTodosOsItens(self):
        return self.dao.listarTodos()
