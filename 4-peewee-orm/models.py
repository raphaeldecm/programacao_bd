from peewee import Model, AutoField, CharField, IntegerField, FloatField
from database import db

class Filme(Model):
    """Modelo que representa a tabela de filmes"""
    
    # Definição das colunas
    id = AutoField(primary_key=True)  # Auto-incremento automático
    nome = CharField(null=False)
    ano = IntegerField(null=False)
    nota = FloatField(null=False)
    
    class Meta:
        database = db  # Conexão com o banco
        table_name = 'filmes'  # Nome da tabela
    
    def __repr__(self):
        """Representação em string do objeto"""
        return f"<Filme(id={self.id}, nome='{self.nome}', ano={self.ano}, nota={self.nota})>"
    
    def to_dict(self):
        """Converte o objeto para dicionário"""
        return {
            'id': self.id,
            'nome': self.nome,
            'ano': self.ano,
            'nota': self.nota
        }
