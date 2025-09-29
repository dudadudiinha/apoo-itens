from model import Item
from database import criar_conexao

class ItemDAO:
    def adicionar(self, item: Item):
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO itens (nome, descricao, quantidade) VALUES (?, ?, ?)",
            (item.get_nome(), item.get_descricao(), item.get_quantidade())
        )
        conn.commit()
        conn.close()

    def listarTodos(self) -> list:
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, descricao, quantidade FROM itens")
        rows = cursor.fetchall()
        conn.close()

        itens = []
        for row in rows:
            id, nome, descricao, quantidade = row
            itens.append(Item(nome=nome, descricao=descricao, quantidade=quantidade, id=id))
        return itens
