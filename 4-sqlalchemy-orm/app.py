import streamlit as st
from database import get_session, init_db
from crud import (
    criar_filme, 
    listar_filmes, 
    buscar_filme_por_id, 
    atualizar_filme, 
    deletar_filme
)

# Configuração da página
st.set_page_config(
    page_title="Sistema de Filmes - SQLAlchemy",
    page_icon="🎬",
    layout="wide",
)

# Inicializar banco de dados
init_db()

# Título principal
st.title("🎬 Sistema de Filmes - SQLAlchemy ORM")
st.markdown("---")

# Criar abas
tab1, tab2, tab3, tab4 = st.tabs(["Adicionar", "Listar", "Atualizar", "Deletar"])

# TAB 1: Adicionar Filme
with tab1:
    st.subheader("Adicionar Novo Filme")
    
    nome = st.text_input("Nome do Filme")
    ano = st.number_input("Ano", min_value=1900, max_value=2030, value=2024)
    nota = st.slider("Nota", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    
    if st.button("Adicionar"):
        if nome.strip():
            session = get_session()
            filme = criar_filme(session, nome, ano, nota)
            session.close()
            
            if filme:
                st.success(f"Filme '{nome}' adicionado com sucesso! (ID: {filme.id})")
                st.balloons()
            else:
                st.error("Erro ao adicionar filme.")
        else:
            st.error("O nome do filme não pode estar vazio.")

# TAB 2: Listar Filmes
with tab2:
    st.subheader("Lista de Filmes")
    
    session = get_session()
    filmes = listar_filmes(session)
    session.close()
    
    if filmes:
        st.write(f"Total de filmes: {len(filmes)}")
        
        for filme in filmes:
            st.write(f"**ID:** {filme.id} | **Nome:** {filme.nome} | "
                    f"**Ano:** {filme.ano} | **Nota:** {filme.nota}")
    else:
        st.info("Nenhum filme cadastrado.")

# TAB 3: Atualizar Filme
with tab3:
    st.subheader("Atualizar Filme")
    
    session = get_session()
    filmes = listar_filmes(session)
    
    if filmes:
        filmes_dict = {f"{f.id} - {f.nome}": f.id for f in filmes}
        
        filme_selecionado = st.selectbox(
            "Selecione o filme para atualizar",
            options=list(filmes_dict.keys())
        )
        
        if filme_selecionado:
            filme_id = filmes_dict[filme_selecionado]
            filme_atual = buscar_filme_por_id(session, filme_id)
            
            if filme_atual:
                st.markdown("---")
                st.write(f"**Filme atual:** {filme_atual.nome} ({filme_atual.ano}) - "
                        f"Nota: {filme_atual.nota}")
                
                novo_nome = st.text_input("Novo Nome", value=filme_atual.nome)
                novo_ano = st.number_input("Novo Ano", min_value=1900, 
                                          max_value=2030, value=filme_atual.ano)
                nova_nota = st.slider("Nova Nota", min_value=0.0, max_value=10.0, 
                                    value=float(filme_atual.nota), step=0.1)
                
                if st.button("Salvar Alterações"):
                    if novo_nome.strip():
                        if atualizar_filme(session, filme_id, novo_nome, novo_ano, nova_nota):
                            st.success("Filme atualizado com sucesso!")
                            st.rerun()
                        else:
                            st.error("Erro ao atualizar filme.")
                    else:
                        st.error("O nome do filme não pode estar vazio.")
    else:
        st.info("Nenhum filme cadastrado.")
    
    session.close()

# TAB 4: Deletar Filme
with tab4:
    st.subheader("Deletar Filme")
    
    session = get_session()
    filmes = listar_filmes(session)
    
    if filmes:
        filmes_dict = {f"{f.id} - {f.nome}": f.id for f in filmes}
        
        filme_selecionado = st.selectbox(
            "Selecione o filme para deletar",
            options=list(filmes_dict.keys()),
            key="delete_select"
        )
        
        if filme_selecionado:
            filme_id = filmes_dict[filme_selecionado]
            filme_atual = buscar_filme_por_id(session, filme_id)
            
            if filme_atual:
                st.markdown("---")
                st.warning(f"Você está prestes a deletar: **{filme_atual.nome} "
                          f"({filme_atual.ano})**")
                
                if st.button("Confirmar Exclusão", type="primary"):
                    if deletar_filme(session, filme_id):
                        st.success(f"Filme '{filme_atual.nome}' deletado com sucesso!")
                        st.rerun()
                    else:
                        st.error("Erro ao deletar filme.")
    else:
        st.info("Nenhum filme cadastrado.")
    
    session.close()

# Rodapé
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>💡 Sistema desenvolvido com SQLAlchemy ORM | 📚 Programação com Banco de Dados</p>
    </div>
    """,
    unsafe_allow_html=True
)
