# Lista de Exercícios - Módulo 2

## Exercícios Práticos de Python + SQLite + POO

Neste módulo, você irá criar aplicações console usando **Programação Orientada a Objetos (POO)**. A ideia é separar as responsabilidades:
- **Classe Database**: gerencia todas as operações no banco de dados (CRUD)
- **Script principal**: gerencia a interface com o usuário (menu, entradas, saídas)

---

## 📚 Estrutura de Arquivos

Para cada exercício, você deve criar **2 arquivos**:

1. `models.py` - Contém a classe Database
2. `sistema_*.py` - Contém o script principal com menu interativo

---

## Exercício 1: Sistema de Tarefas (To-Do List)

Crie um sistema para gerenciar tarefas do dia a dia.

### Estrutura da tabela:
```sql
CREATE TABLE tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    prioridade TEXT NOT NULL,
    concluida BOOLEAN DEFAULT 0,
    data_criacao TEXT NOT NULL
);
```

### Arquivo: `models.py`

Crie a classe `Database` com os seguintes métodos:

```python
class Database:
    def __init__(self, db_name="tarefas.db")
    def create_table()
    def criar_tarefa(descricao, prioridade, data_criacao)
    def listar_tarefas()
    def listar_tarefas_pendentes()
    def buscar_tarefa_por_id(tarefa_id)
    def marcar_como_concluida(tarefa_id)
    def deletar_tarefa(tarefa_id)
```

### Arquivo: `sistema_tarefas.py`

Crie um menu interativo com as seguintes opções:

```
1. Adicionar tarefa
2. Listar todas as tarefas
3. Listar tarefas pendentes
4. Marcar tarefa como concluída
5. Deletar tarefa
0. Sair
```

**Dicas:**
- Use `from datetime import date` para pegar a data atual: `date.today()`
- Prioridades sugeridas: "Baixa", "Média", "Alta"
- Exiba ✓ para tarefas concluídas e ✗ para pendentes

---

## Exercício 2: Catálogo de Músicas

Sistema para gerenciar um catálogo de músicas favoritas.

### Estrutura da tabela:
```sql
CREATE TABLE musicas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    artista TEXT NOT NULL,
    album TEXT,
    duracao INTEGER NOT NULL,
    genero TEXT NOT NULL
);
```

### Arquivo: `models.py`

Crie a classe `Database` com os seguintes métodos:

```python
class Database:
    def __init__(self, db_name="musicas.db")
    def create_table()
    def adicionar_musica(titulo, artista, album, duracao, genero)
    def listar_musicas()
    def buscar_por_artista(artista)
    def buscar_por_genero(genero)
    def atualizar_musica(musica_id, titulo=None, artista=None, album=None, duracao=None, genero=None)
    def deletar_musica(musica_id)
```

### Arquivo: `sistema_musicas.py`

Crie um menu com:

```
1. Adicionar música
2. Listar todas as músicas
3. Buscar por artista
4. Buscar por gênero
5. Atualizar música
6. Deletar música
0. Sair
```

**Dicas:**
- Duração em segundos (ex: 180 para 3 minutos)
- Crie uma função para converter segundos em formato MM:SS
- Gêneros sugeridos: Rock, Pop, Jazz, Clássica, Eletrônica

---

## Exercício 3: Controle de Despesas Pessoais

Sistema para controlar gastos mensais.

### Estrutura da tabela:
```sql
CREATE TABLE despesas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    valor REAL NOT NULL,
    categoria TEXT NOT NULL,
    data TEXT NOT NULL,
    pago BOOLEAN DEFAULT 0
);
```

### Arquivo: `models.py`

Crie a classe `Database` com os seguintes métodos:

```python
class Database:
    def __init__(self, db_name="despesas.db")
    def create_table()
    def adicionar_despesa(descricao, valor, categoria, data)
    def listar_despesas()
    def listar_despesas_pendentes()
    def buscar_por_categoria(categoria)
    def calcular_total_gasto()
    def marcar_como_pago(despesa_id)
    def deletar_despesa(despesa_id)
```

### Arquivo: `sistema_despesas.py`

Crie um menu com:

```
1. Adicionar despesa
2. Listar todas as despesas
3. Listar despesas pendentes
4. Filtrar por categoria
5. Ver total gasto
6. Marcar como pago
7. Deletar despesa
0. Sair
```

**Dicas:**
- Categorias: Alimentação, Transporte, Saúde, Lazer, Contas, Outros
- Formate valores monetários: `f"R$ {valor:.2f}"`
- Use `date.today().strftime("%d/%m/%Y")` para formatar datas

---

## Exercício 4: Agenda de Contatos

Sistema para gerenciar contatos telefônicos.

### Estrutura da tabela:
```sql
CREATE TABLE contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT,
    categoria TEXT DEFAULT 'Pessoal',
    favorito BOOLEAN DEFAULT 0
);
```

### Arquivo: `models.py`

Crie a classe `Database` com os seguintes métodos:

```python
class Database:
    def __init__(self, db_name="contatos.db")
    def create_table()
    def adicionar_contato(nome, telefone, email, categoria)
    def listar_contatos()
    def listar_favoritos()
    def buscar_por_nome(nome)
    def marcar_como_favorito(contato_id)
    def atualizar_contato(contato_id, nome=None, telefone=None, email=None, categoria=None)
    def deletar_contato(contato_id)
```

### Arquivo: `sistema_contatos.py`

Crie um menu com:

```
1. Adicionar contato
2. Listar todos os contatos
3. Listar favoritos
4. Buscar por nome
5. Marcar como favorito
6. Atualizar contato
7. Deletar contato
0. Sair
```

**Dicas:**
- Categorias: Pessoal, Trabalho, Família, Amigos
- Use ★ para marcar favoritos
- Valide formato de email (deve conter @)

---

## Exercício 5: Inventário de Jogos

Sistema para catalogar jogos de videogame.

### Estrutura da tabela:
```sql
CREATE TABLE jogos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    plataforma TEXT NOT NULL,
    genero TEXT NOT NULL,
    ano INTEGER NOT NULL,
    zerado BOOLEAN DEFAULT 0,
    nota REAL
);
```

### Arquivo: `models.py`

Crie a classe `Database` com os seguintes métodos:

```python
class Database:
    def __init__(self, db_name="jogos.db")
    def create_table()
    def adicionar_jogo(titulo, plataforma, genero, ano, nota=None)
    def listar_jogos()
    def listar_por_plataforma(plataforma)
    def listar_nao_zerados()
    def marcar_como_zerado(jogo_id)
    def atualizar_nota(jogo_id, nota)
    def deletar_jogo(jogo_id)
```

### Arquivo: `sistema_jogos.py`

Crie um menu com:

```
1. Adicionar jogo
2. Listar todos os jogos
3. Filtrar por plataforma
4. Listar jogos não zerados
5. Marcar como zerado
6. Avaliar jogo (dar nota)
7. Deletar jogo
0. Sair
```

**Dicas:**
- Plataformas: PC, PlayStation, Xbox, Nintendo Switch, Mobile
- Gêneros: Ação, RPG, Aventura, Estratégia, Esporte, Puzzle
- Nota de 0 a 10

---

## 📋 Instruções Gerais

### Estrutura da Classe Database

Sua classe deve seguir este padrão:

```python
import sqlite3

class Database:
    def __init__(self, db_name="nome_banco.db"):
        """Inicializa a conexão e cria a tabela."""
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()
    
    def create_table(self):
        """Cria a tabela se não existir."""
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS nome_tabela (
                    -- estrutura da tabela
                )
            """)
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao criar tabela: {e}")
            return False
    
    def criar_item(self, ...):
        """Insere um novo item."""
        try:
            self.cursor.execute("""
                INSERT INTO tabela (...) VALUES (?, ?, ...)
            """, (...))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao inserir: {e}")
            return False
    
    # ... demais métodos
```

### Estrutura do Script Principal

```python
from models import Database

def limpar_tela():
    """Limpa a tela do terminal."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Pausa e aguarda Enter."""
    input("\nPressione Enter para continuar...")

def mostrar_menu():
    """Exibe o menu principal."""
    print("\n" + "="*40)
    print("      TÍTULO DO SISTEMA")
    print("="*40)
    print("1. Opção 1")
    print("2. Opção 2")
    # ... mais opções
    print("0. Sair")
    print("="*40)

def funcao_opcao_1(db):
    """Implementa a opção 1."""
    print("\n--- TÍTULO DA OPÇÃO ---")
    # Obter dados do usuário
    # Validar dados
    # Chamar método da classe Database
    # Mostrar resultado

def main():
    """Função principal."""
    print("Inicializando sistema...")
    db = Database()
    
    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            limpar_tela()
            funcao_opcao_1(db)
            pausar()
            limpar_tela()
        # ... demais opções
        elif opcao == "0":
            print("\nObrigado por usar o sistema!")
            break
        else:
            print("❌ Opção inválida!")
            pausar()
            limpar_tela()

if __name__ == "__main__":
    main()
```

---

## ✅ Checklist de Entrega

Para cada exercício, certifique-se de:

- [ ] Criar arquivo `models.py` com a classe Database
- [ ] Criar arquivo `sistema_*.py` com menu interativo
- [ ] Implementar todos os métodos solicitados
- [ ] Usar consultas parametrizadas (com `?`)
- [ ] Tratar erros com try/except
- [ ] Validar entradas do usuário
- [ ] Adicionar comentários explicativos
- [ ] Testar todas as funcionalidades
- [ ] Usar `limpar_tela()` e `pausar()` para melhor UX
- [ ] Formatar saídas de forma organizada

---

## 🎯 Diferenciais (Opcional)

Para impressionar, adicione:

- Confirmação antes de deletar itens
- Busca com filtros múltiplos
- Estatísticas e relatórios
- Validação de dados mais robusta
- Cores no terminal (biblioteca `colorama`)
- Exportação de dados para CSV

---

## 💡 Dicas Importantes

1. **Separação de responsabilidades**: A classe Database só cuida do banco. O script principal só cuida da interface.

2. **Reutilização**: Métodos como `buscar_por_id()` podem ser usados dentro de outros métodos.

3. **Validação**: Sempre valide dados ANTES de enviar para o banco.

4. **Feedback**: Sempre mostre mensagens claras de sucesso ou erro.

5. **Teste incremental**: Teste cada método assim que criar.

---

## 📚 Recursos de Apoio

- Documentação SQLite: https://www.sqlite.org/docs.html
- Python sqlite3: https://docs.python.org/3/library/sqlite3.html
- POO em Python: https://docs.python.org/3/tutorial/classes.html

---

**Bons estudos! 🚀**
