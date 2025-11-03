import sqlite3

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('titulo.db')
cursor = conn.cursor()  # Obtendo o cursor para executar comandos SQL

# Atualizando dados
id = 1  # ID do filme a ser atualizado
cursor.execute(
  """
    UPDATE filmes SET nome = ?
    WHERE id = ?
  """,
  ('O Senhor dos Anéis: A Sociedade do Anel (Edição Estendida)', id))

# Salvando as mudanças e fechando a conexão
conn.commit()
conn.close()
print("Dados atualizados com sucesso na tabela 'filmes'!")