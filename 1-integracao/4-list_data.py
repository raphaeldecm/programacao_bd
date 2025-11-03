import sqlite3

# Conexão com o banco de dados SQLite
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()  # Obtendo o cursor para executar comandos SQL

# Consultando todos os dados da tabela 'filmes'
data = cursor.execute("SELECT * FROM filmes")

print(data)  # Exibindo o objeto do cursor
print(data.fetchall())  # Exibindo todos os registros retornados pela consulta