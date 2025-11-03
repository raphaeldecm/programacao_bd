import sqlite3

# 1 - Conectando ao banco de dados
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()  # Obtendo o cursor para executar comandos SQL

# 2 - Inserindo dados na tabela
cursor.execute("""
    INSERT INTO filmes (nome, ano, nota) VALUES
    ('O Senhor dos Anéis: A Sociedade do Anel', 2001, 8.8),
    ('O Senhor dos Anéis: As Duas Torres', 2002, 8.7),
    ('O Senhor dos Anéis: O Retorno do Rei', 2003, 9.0)
""")

# 3 - Salvando as mudanças e fechando a conexão
conexao.commit()
conexao.close()
print("Dados inseridos com sucesso na tabela 'filmes'!")