"""
Utilitários para formatação e validação de dados na aplicação console.
"""


def formatar_filme(filme_data):
    """
    Formata os dados de um filme para exibição.
    
    Args:
        filme_data (tuple): Tupla com (id, nome, ano, nota)
        
    Returns:
        str: String formatada do filme
    """
    if not filme_data or len(filme_data) != 4:
        return "Dados do filme inválidos"
    
    id_filme, nome, ano, nota = filme_data
    return f"[{id_filme:02d}] {nome} ({ano}) - Nota: {nota:.1f}"


def formatar_lista_filmes(filmes):
    """
    Formata uma lista de filmes para exibição.
    
    Args:
        filmes (list): Lista de tuplas com dados dos filmes
        
    Returns:
        str: String formatada com todos os filmes
    """
    if not filmes:
        return "Nenhum filme encontrado."
    
    resultado = []
    for filme in filmes:
        resultado.append(formatar_filme(filme))
    
    resultado.append(f"Total: {len(filmes)} filme(s)")
    
    return "\n".join(resultado)


def validar_ano(ano_str):
    """
    Valida e converte uma string para ano.
    
    Args:
        ano_str (str): String do ano
        
    Returns:
        int: Ano válido ou None se inválido
    """
    try:
        ano = int(ano_str)
        if 1800 <= ano <= 2030:  # Faixa razoável de anos para filmes
            return ano
        else:
            print("Ano deve estar entre 1800 e 2030.")
            return None
    except ValueError:
        print("Ano deve ser um número inteiro.")
        return None


def validar_nota(nota_str):
    """
    Valida e converte uma string para nota.
    
    Args:
        nota_str (str): String da nota
        
    Returns:
        float: Nota válida ou None se inválida
    """
    try:
        nota = float(nota_str)
        if 0.0 <= nota <= 10.0:
            return nota
        else:
            print("Nota deve estar entre 0.0 e 10.0.")
            return None
    except ValueError:
        print("Nota deve ser um número.")
        return None


def validar_id(id_str):
    """
    Valida e converte uma string para ID.
    
    Args:
        id_str (str): String do ID
        
    Returns:
        int: ID válido ou None se inválido
    """
    try:
        id_filme = int(id_str)
        if id_filme > 0:
            return id_filme
        else:
            print("ID deve ser um número positivo.")
            return None
    except ValueError:
        print("ID deve ser um número inteiro.")
        return None


def validar_nome(nome):
    """
    Valida o nome do filme.
    
    Args:
        nome (str): Nome do filme
        
    Returns:
        str: Nome válido ou None se inválido
    """
    nome = nome.strip()
    if len(nome) < 1:
        print("Nome do filme não pode estar vazio.")
        return None
    elif len(nome) > 200:
        print("Nome do filme é muito longo (máximo 200 caracteres).")
        return None
    else:
        return nome


def limpar_tela():
    """Limpa a tela do terminal."""
    import os
    os.system('clear' if os.name == 'posix' else 'cls')


def pausar():
    """Pausa a execução aguardando o usuário pressionar Enter."""
    try:
        input("\nPressione Enter para continuar...")
    except EOFError:
        pass


def obter_confirmacao(mensagem):
    """
    Solicita confirmação do usuário.
    
    Args:
        mensagem (str): Mensagem de confirmação
        
    Returns:
        bool: True se confirmado, False caso contrário
    """
    resposta = input(f"{mensagem} (s/N): ").strip().lower()
    return resposta in ['s', 'sim']