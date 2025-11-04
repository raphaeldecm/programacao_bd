import sqlite3

# 1 - Conectando ao banco de dados
conexao = sqlite3.connect('titulo.db')

# 2 - Obtendo o cursor
cursor = conexao.cursor() # Obtendo o cursor para executar comandos SQL

# 3 - Criando a tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ano INTEGER NOT NULL,
        nota REAL NOT NULL               
    )
""")

# 4 - Fechando a conexão
conexao.close()  # Fechando a conexão com o banco de dados
print("Tabela 'filmes' criada com sucesso!")