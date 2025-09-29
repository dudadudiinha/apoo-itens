import sqlite3

def criar_conexao():
    conn = sqlite3.connect("itens.db")
    return conn

def criar_tabela():
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS itens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            quantidade INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

criar_tabela() # tabela criada assim que o arquivo é importado
