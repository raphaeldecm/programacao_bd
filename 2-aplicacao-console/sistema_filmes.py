#!/usr/bin/env python3
"""
Sistema de Filmes - Versão Simples
Script educativo para demonstrar uso da classe Database
"""

from models import Database


def limpar_tela():
    """Limpa a tela (funciona no Windows e Linux)."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """Pausa e aguarda o usuário pressionar Enter."""
    input("\nPressione Enter para continuar...")


def mostrar_menu():
    """Exibe o menu principal."""
    print("\n" + "="*40)
    print("      SISTEMA DE FILMES")
    print("="*40)
    print("1. Adicionar filme")
    print("2. Listar filmes")
    print("3. Buscar filme por ID")
    print("4. Atualizar filme")
    print("5. Deletar filme")
    print("0. Sair")
    print("="*40)


def adicionar_filme(db):
    """Adiciona um novo filme."""
    print("\n--- ADICIONAR FILME ---")
    
    # Obter dados do usuário
    nome = input("Nome do filme: ").strip()
    if not nome:
        print(" Nome não pode estar vazio!")
        return
    
    try:
        ano = int(input("Ano de lançamento: "))
        nota = float(input("Nota (0.0 a 10.0): "))
    except ValueError:
        print(" Ano deve ser um número inteiro e nota um número decimal!")
        return
    
    if ano < 1900 or ano > 2030:
        print(" Ano deve estar entre 1900 e 2030!")
        return
    
    if nota < 0.0 or nota > 10.0:
        print(" Nota deve estar entre 0.0 e 10.0!")
        return
    
    # Inserir no banco
    if db.criar_filme(nome, ano, nota):
        print("Filme adicionado com sucesso!")
    else:
        print("Erro ao adicionar filme!")


def listar_filmes(db):
    """Lista todos os filmes."""
    print("\n--- LISTA DE FILMES ---")
    
    filmes = db.listar_filmes()
    
    if not filmes:
        print("Nenhum filme encontrado.")
        return
    
    print(f"\nTotal de filmes: {len(filmes)}")
    print("-" * 60)
    
    for filme in filmes:
        id_filme, nome, ano, nota = filme
        print(f"ID: {id_filme:2d} | {nome} ({ano}) - Nota: {nota}")
    
    print("-" * 60)


def buscar_filme(db):
    """Busca um filme por ID."""
    print("\n--- BUSCAR FILME ---")
    
    try:
        filme_id = int(input("Digite o ID do filme: "))
    except ValueError:
        print(" ID deve ser um número inteiro!")
        return
    
    filme = db.buscar_filme_por_id(filme_id)
    
    if filme:
        id_filme, nome, ano, nota = filme
        print("\nFilme encontrado:")
        print(f"ID: {id_filme}")
        print(f"Nome: {nome}")
        print(f"Ano: {ano}")
        print(f"Nota: {nota}")
    else:
        print(" Filme não encontrado!")


def atualizar_filme(db):
    """Atualiza um filme existente."""
    print("\n--- ATUALIZAR FILME ---")
    
    try:
        filme_id = int(input("Digite o ID do filme para atualizar: "))
    except ValueError:
        print(" ID deve ser um número inteiro!")
        return
    
    # Verificar se filme existe
    filme = db.buscar_filme_por_id(filme_id)
    if not filme:
        print(" Filme não encontrado!")
        return
    
    # Mostrar dados atuais
    id_filme, nome_atual, ano_atual, nota_atual = filme
    print("\nFilme atual:")
    print(f"Nome: {nome_atual}")
    print(f"Ano: {ano_atual}")
    print(f"Nota: {nota_atual}")
    
    print("\nDigite os novos dados (deixe em branco para manter o atual):")
    
    # Obter novos dados
    novo_nome = input(f"Novo nome [{nome_atual}]: ").strip()
    if not novo_nome:
        novo_nome = None
    
    novo_ano_str = input(f"Novo ano [{ano_atual}]: ").strip()
    novo_ano = None
    if novo_ano_str:
        try:
            novo_ano = int(novo_ano_str)
            if novo_ano < 1900 or novo_ano > 2030:
                print(" Ano deve estar entre 1900 e 2030!")
                return
        except ValueError:
            print(" Ano deve ser um número inteiro!")
            return
    
    nova_nota_str = input(f"Nova nota [{nota_atual}]: ").strip()
    nova_nota = None
    if nova_nota_str:
        try:
            nova_nota = float(nova_nota_str)
            if nova_nota < 0.0 or nova_nota > 10.0:
                print(" Nota deve estar entre 0.0 e 10.0!")
                return
        except ValueError:
            print(" Nota deve ser um número decimal!")
            return
    
    # Atualizar no banco
    if db.atualizar_filme(filme_id, novo_nome, novo_ano, nova_nota):
        print("Filme atualizado com sucesso!")
    else:
        print(" Erro ao atualizar filme!")


def deletar_filme(db):
    """Deleta um filme."""
    print("\n--- DELETAR FILME ---")
    
    try:
        filme_id = int(input("Digite o ID do filme para deletar: "))
    except ValueError:
        print(" ID deve ser um número inteiro!")
        return
    
    # Verificar se filme existe
    filme = db.buscar_filme_por_id(filme_id)
    if not filme:
        print(" Filme não encontrado!")
        return
    
    # Mostrar dados do filme
    id_filme, nome, ano, nota = filme
    print("\nFilme a ser deletado:")
    print(f"ID: {id_filme}")
    print(f"Nome: {nome}")
    print(f"Ano: {ano}")
    print(f"Nota: {nota}")
    
    # Confirmar deleção
    confirmacao = input("\nTem certeza que deseja deletar? (s/N): ").strip().lower()
    
    if confirmacao == 's':
        if db.deletar_filme(filme_id):
            print("Filme deletado com sucesso!")
        else:
            print(" Erro ao deletar filme!")
    else:
        print(" Operação cancelada!")


def main():
    print("Inicializando sistema de filmes...")
    
    # Criar conexão com banco
    db = Database()
    
    while True:
        mostrar_menu()
        
        try:
            opcao = input("\nEscolha uma opção: ").strip()
        except KeyboardInterrupt:
            print("\n\nSaindo do programa...")
            break
        
        if opcao == "1":
            limpar_tela()
            adicionar_filme(db)
            pausar()
            limpar_tela()
        
        elif opcao == "2":
            limpar_tela()
            listar_filmes(db)
            pausar()
            limpar_tela()
        
        elif opcao == "3":
            limpar_tela()
            buscar_filme(db)
            pausar()
            limpar_tela()
        
        elif opcao == "4":
            limpar_tela()
            atualizar_filme(db)
            pausar()
            limpar_tela()
        
        elif opcao == "5":
            limpar_tela()
            deletar_filme(db)
            pausar()
            limpar_tela()
        
        elif opcao == "0":
            print("\nObrigado por usar o sistema!")
            break
        
        else:
            print(" Opção inválida! Tente novamente.")
            pausar()
            limpar_tela()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nErro inesperado: {e}")
        print("O programa será encerrado.")