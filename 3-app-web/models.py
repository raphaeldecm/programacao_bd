import sqlite3

class Database:

  def __init__(self, db_name="filmes.db", table_name="filmes"):
      self.db_name = db_name
      # check_same_thread=False permite usar a conexão em diferentes threads (necessário para Streamlit)
      self.connection = sqlite3.connect(db_name, check_same_thread=False)
      self.cursor = self.connection.cursor()
      self.create_table(table_name)
  
  def create_table(self, table_name="filmes"):
      """Cria a tabela de filmes se não existir."""
      try:
        self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL               
          )
        """)
        self.connection.commit()
        return True
      except sqlite3.Error as e:
          print(f"Erro ao criar tabela: {e}")
          return False

  def criar_filme(self, nome, ano, nota):
      """Insere um novo filme na tabela."""
      try:
          self.cursor.execute("""
              INSERT INTO filmes (nome, ano, nota) VALUES (?, ?, ?)
          """, (nome, ano, nota))
          self.connection.commit()
          return True
      except sqlite3.Error as e:
          print(f"Erro ao inserir filme: {e}")
          return False
  
  def listar_filmes(self):
      """Retorna todos os filmes da tabela."""
      try:
          self.cursor.execute(
            """
              SELECT id, nome, ano, nota FROM filmes ORDER BY ano DESC
            """
          )
          return self.cursor.fetchall()
      except sqlite3.Error as e:
          print(f"Erro ao listar filmes: {e}")
          return []
  
  def buscar_filme_por_id(self, filme_id):
      """Busca um filme pelo ID."""
      try:
          self.cursor.execute(
              """
                SELECT id, nome, ano, nota FROM filmes WHERE id = ?
              """,
              (filme_id,)
          )
          return self.cursor.fetchone()
      except sqlite3.Error as e:
          print(f"Erro ao buscar filme: {e}")
          return None

  def atualizar_filme(self, filme_id, nome=None, ano=None, nota=None):
      """Atualiza os dados de um filme pelo ID."""
      filme = self.buscar_filme_por_id(filme_id)
      if not filme:
          return False

      # Mantém valores não alterados se não forem fornecidos novos
      novo_nome = nome if nome is not None else filme[1]
      novo_ano = ano if ano is not None else filme[2]
      nova_nota = nota if nota is not None else filme[3]

      try:
          self.cursor.execute(
              """
                UPDATE filmes SET nome = ?, ano = ?, nota = ? WHERE id = ?
              """,
              (novo_nome, novo_ano, nova_nota, filme_id)
          )
          self.connection.commit()
          return self.cursor.rowcount > 0 # Retorna True se a atualização foi bem-sucedida self.cursor.rowcount retorna o número de linha modificadas
      except sqlite3.Error as e:
          print(f"Erro ao atualizar filme: {e}")
          return False

  def deletar_filme(self, filme_id):
      """Deleta um filme pelo ID."""
      try:
          self.cursor.execute(
              """
                DELETE FROM filmes WHERE id = ?
              """,
              (filme_id,)
          )
          self.connection.commit()
          return self.cursor.rowcount > 0
      except sqlite3.Error as e:
          print(f"Erro ao deletar filme: {e}")
          return False