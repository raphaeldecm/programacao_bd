# Módulo 2: Aplicação Console com POO

## 📖 Objetivo

Neste módulo, você aprenderá a criar aplicações console mais estruturadas usando **Programação Orientada a Objetos (POO)** para organizar o código de forma profissional.

## 🎯 Conceitos Abordados

- **Separação de responsabilidades** (Separation of Concerns)
- **Classes para gerenciamento de banco de dados**
- **Interface de usuário via terminal**
- **CRUD completo com POO**
- **Boas práticas de organização de código**

## 📁 Estrutura de Arquivos

Este módulo demonstra uma aplicação dividida em dois arquivos principais:

```
2-aplicacao-console/
├── models.py           # Classe Database (lógica de banco de dados)
├── sistema_filmes.py   # Interface do usuário (menu e interações)
└── EXERCICIOS.md       # Lista de exercícios práticos
```

## 🔧 Arquivos do Projeto

### `models.py`

Contém a classe `Database` responsável por **todas as operações no banco de dados**:

- Conexão com SQLite
- Criação de tabelas
- Operações CRUD (Create, Read, Update, Delete)
- Tratamento de erros de banco de dados

**Princípio:** Esta classe não sabe nada sobre menus ou interface. Ela apenas gerencia dados.

### `sistema_filmes.py`

Contém a **interface do usuário** e a lógica de apresentação:

- Menu interativo
- Validação de entradas
- Formatação de saídas
- Controle de fluxo da aplicação

**Princípio:** Este arquivo não sabe como os dados são armazenados. Ele apenas usa a classe Database.

## 🚀 Como Executar

1. Certifique-se de estar no diretório correto:
```bash
cd 2-aplicacao-console
```

2. Execute o sistema:
```bash
python3 sistema_filmes.py
```

## 💡 Vantagens da Arquitetura

### 1. **Reusabilidade**
A classe `Database` pode ser importada e usada em diferentes scripts.

### 2. **Manutenção**
Mudanças no banco de dados ficam isoladas no `models.py`. Mudanças na interface ficam no script principal.

### 3. **Testabilidade**
Você pode testar métodos da classe Database independentemente da interface.

### 4. **Escalabilidade**
Facilita adicionar novas funcionalidades sem bagunçar o código.

## 📚 Exemplo de Uso

### Importando a classe Database

```python
from models import Database

# Criar conexão
db = Database()

# Usar métodos
db.criar_filme("Matrix", 1999, 9.5)
filmes = db.listar_filmes()
```

### Estrutura da Classe Database

```python
class Database:
    def __init__(self, db_name="filmes.db"):
        # Inicializa conexão
        
    def create_table(self):
        # Cria tabelas
        
    def criar_filme(self, nome, ano, nota):
        # INSERT
        
    def listar_filmes(self):
        # SELECT ALL
        
    def buscar_filme_por_id(self, filme_id):
        # SELECT ONE
        
    def atualizar_filme(self, filme_id, ...):
        # UPDATE
        
    def deletar_filme(self, filme_id):
        # DELETE
```

## 🎓 O que Você Vai Aprender

- [x] Criar classes em Python
- [x] Organizar código em múltiplos arquivos
- [x] Importar e usar classes personalizadas
- [x] Separar lógica de negócio da interface
- [x] Criar menus interativos
- [x] Validar entradas do usuário
- [x] Tratar erros adequadamente
- [x] Aplicar boas práticas de POO

## 📝 Exercícios

Confira o arquivo [EXERCICIOS.md](EXERCICIOS.md) para praticar criando seus próprios sistemas:

1. **Sistema de Tarefas** - To-Do List
2. **Catálogo de Músicas** - Gerenciador de playlist
3. **Controle de Despesas** - Finanças pessoais
4. **Agenda de Contatos** - Lista telefônica
5. **Inventário de Jogos** - Coleção de games

## 🔍 Padrão de Desenvolvimento

Para cada exercício, siga este fluxo:

1. **Planejar** - Defina a estrutura da tabela
2. **Criar models.py** - Implemente a classe Database
3. **Testar métodos** - Teste cada método individualmente
4. **Criar sistema** - Implemente o menu e interface
5. **Integrar** - Conecte interface com Database
6. **Validar** - Teste toda a aplicação

## 🛠️ Dicas de Desenvolvimento

### Testando a Classe Database

Você pode testar métodos diretamente no Python interativo:

```python
python3

>>> from models import Database
>>> db = Database()
>>> db.criar_filme("Inception", 2010, 9.0)
True
>>> db.listar_filmes()
[(1, 'Inception', 2010, 9.0)]
```

### Debug

Adicione prints dentro dos métodos para debug:

```python
def criar_filme(self, nome, ano, nota):
    print(f"DEBUG: Inserindo {nome}, {ano}, {nota}")  # Debug
    try:
        self.cursor.execute(...)
```

## 📖 Recursos Adicionais

- [Python Classes Tutorial](https://docs.python.org/3/tutorial/classes.html)
- [SQLite with Python](https://docs.python.org/3/library/sqlite3.html)
- [Clean Code Principles](https://www.python.org/dev/peps/pep-0008/)

## 🎯 Próximos Passos

Após dominar este módulo, você estará pronto para:

- **Módulo 3:** Aplicações Web com Flask
- **Módulo 4:** SQLAlchemy ORM
- Criar APIs REST
- Conectar com bancos de dados mais robustos

---

**Bons estudos! 🚀**
