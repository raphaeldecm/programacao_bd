from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Criar engine de conexão com SQLite
# echo=True mostra os SQL gerados (útil para aprendizado)
engine = create_engine('sqlite:///filmes.db', 
                      echo=False,
                      connect_args={"check_same_thread": False})

# Criar classe base para os modelos
Base = declarative_base()

# Criar fábrica de sessões
SessionLocal = sessionmaker(bind=engine, 
                           autocommit=False, 
                           autoflush=False)

def get_session():
    """Retorna uma nova sessão do banco de dados"""
    return SessionLocal()

def init_db():
    """Inicializa o banco de dados criando todas as tabelas"""
    Base.metadata.create_all(bind=engine)
