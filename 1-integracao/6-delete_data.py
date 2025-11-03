import sqlite3

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('titulo.db')
cursor = conn.cursor()  # Obtendo o cursor para executar comandos SQL

# Deletando dados
id = (2,3) # IDs dos filmes a serem deletados. Deve ser uma tupla ou lista
cursor.execute(
  """
    DELETE FROM filmes 
    WHERE id in (?, ?)
  """,
  id
)

# Salvando as mudanças e fechando a conexão
conn.commit()
conn.close()
print("Dados deletados com sucesso na tabela 'filmes'!")