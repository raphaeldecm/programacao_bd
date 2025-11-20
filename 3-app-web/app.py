import streamlit as st
from models import Database

# Configuração da página
st.set_page_config(
    page_title="Sistema de Filmes",
    page_icon="🎬",
    layout="wide",
)

# Inicializar banco de dados
# st.cache_resource evita criar várias conexões a cada interação com a aplicação
@st.cache_resource
def get_database():
    return Database("filmes.db")

db = get_database()

# Título principal
st.title("🎬 Sistema de Filmes")
st.markdown("---")

# Criar abas para as operações CRUD
tab1, tab2, tab3, tab4 = st.tabs(["Adicionar", "Listar", "Atualizar", "Deletar"])

# TAB 1: Adicionar Filme
with tab1:
    st.subheader("Adicionar Novo Filme")
    
    nome = st.text_input("Nome do Filme")
    ano = st.number_input("Ano", min_value=1900, max_value=2030, value=2024)
    nota = st.slider("Nota", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    
    if st.button("Adicionar"):
        if nome.strip():
            if db.criar_filme(nome, ano, nota):
                st.success("Filme adicionado com sucesso!")
                st.balloons()
            else:
                st.error("Erro ao adicionar filme.")
        else:
            st.error("O nome do filme não pode estar vazio.")

# TAB 2: Listar Filmes
with tab2:
    st.subheader("Lista de Filmes")
    
    filmes = db.listar_filmes()
    
    if filmes:
        st.write(f"Total de filmes: {len(filmes)}")
        
        # Exibir filmes em formato de tabela simples
        for filme in filmes:
            st.write(f"**ID:** {filme[0]} | **Nome:** {filme[1]} | **Ano:** {filme[2]} | **Nota:** {filme[3]}")
    else:
        st.info("Nenhum filme cadastrado.")

# TAB 3: Atualizar Filme
with tab3:
    st.subheader("Atualizar Filme")
    
    filmes = db.listar_filmes()
    
    if filmes:
        # Criar dicionário de filmes para seleção
        filmes_dict = {f"{filme[0]} - {filme[1]}": filme[0] for filme in filmes}
        
        filme_selecionado = st.selectbox(
            "Selecione o filme para atualizar",
            options=list(filmes_dict.keys())
        )
        
        if filme_selecionado:
            filme_id = filmes_dict[filme_selecionado]
            filme_atual = db.buscar_filme_por_id(filme_id)
            
            if filme_atual:
                st.markdown("---")
                st.write(f"**Filme atual:** {filme_atual[1]} ({filme_atual[2]}) - Nota: {filme_atual[3]}")
                
                novo_nome = st.text_input("Novo Nome", value=filme_atual[1])
                novo_ano = st.number_input("Novo Ano", min_value=1900, max_value=2030, value=int(filme_atual[2]))
                nova_nota = st.slider("Nova Nota", min_value=0.0, max_value=10.0, value=float(filme_atual[3]), step=0.1)
                
                if st.button("Salvar Alterações"):
                    if novo_nome.strip():
                        if db.atualizar_filme(filme_id, novo_nome, novo_ano, nova_nota):
                            st.success("Filme atualizado com sucesso!")
                            st.rerun()
                        else:
                            st.error("Erro ao atualizar filme.")
                    else:
                        st.error("O nome do filme não pode estar vazio.")
    else:
        st.info("Nenhum filme cadastrado.")

# TAB 4: Deletar Filme
with tab4:
    st.subheader("Deletar Filme")
    
    filmes = db.listar_filmes()
    
    if filmes:
        # Criar dicionário de filmes para seleção
        filmes_dict = {f"{filme[0]} - {filme[1]}": filme[0] for filme in filmes}
        
        filme_selecionado = st.selectbox(
            "Selecione o filme para deletar",
            options=list(filmes_dict.keys()),
            key="delete_select"
        )
        
        if filme_selecionado:
            filme_id = filmes_dict[filme_selecionado]
            filme_atual = db.buscar_filme_por_id(filme_id)
            
            if filme_atual:
                st.markdown("---")
                st.warning(f"Você está prestes a deletar: **{filme_atual[1]} ({filme_atual[2]})**")
                
                if st.button("Confirmar Exclusão", type="primary"):
                    if db.deletar_filme(filme_id):
                        st.success(f"Filme '{filme_atual[1]}' deletado com sucesso!")
                        st.rerun()
                    else:
                        st.error("Erro ao deletar filme.")
    else:
        st.info("Nenhum filme cadastrado.")

# Rodapé
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>💡 Sistema desenvolvido com Streamlit | 📚 Programação com Banco de Dados</p>
    </div>
    """,
    unsafe_allow_html=True
)
