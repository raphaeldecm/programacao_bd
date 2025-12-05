from peewee import SqliteDatabase

# Criar conexão com o banco de dados SQLite
# pragmas ajudam com performance e compatibilidade
db = SqliteDatabase('filmes.db', pragmas={
    'journal_mode': 'wal',  # Write-Ahead Logging para melhor concorrência
    'cache_size': -1024 * 64,  # 64MB de cache
    'foreign_keys': 1,  # Habilitar chaves estrangeiras
    'ignore_check_constraints': 0,
    'synchronous': 0
})

def init_db():
    """Inicializa o banco de dados criando todas as tabelas"""
    from models import Filme
    db.connect()
    db.create_tables([Filme], safe=True)
    
def close_db():
    """Fecha a conexão com o banco de dados"""
    if not db.is_closed():
        db.close()
