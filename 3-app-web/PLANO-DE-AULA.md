# 🎓 Plano de Aula - Módulo 3: Interface Web com Streamlit

## 📋 Informações da Aula

**Módulo:** 3 - Aplicação Web com Streamlit  
**Duração sugerida:** 4-6 horas (2-3 aulas)  
**Pré-requisitos:** Módulos 1 e 2 concluídos  
**Nível:** Ensino Médio/Técnico

---

## 🎯 Objetivos de Aprendizagem

Ao final desta aula, os alunos serão capazes de:

1. ✅ Criar e gerenciar ambientes virtuais Python
2. ✅ Instalar e configurar bibliotecas usando pip
3. ✅ Construir interfaces web interativas com Streamlit
4. ✅ Integrar aplicações web com banco de dados SQLite
5. ✅ Implementar operações CRUD em interface gráfica
6. ✅ Aplicar boas práticas de organização de projetos

---

## 📚 Estrutura da Aula

### **AULA 1: Introdução e Configuração (2h)**

#### Parte 1: Conceitos Teóricos (30 min)
- O que são aplicações web?
- Por que usar Streamlit?
- Diferença entre aplicação console e web
- Demonstração de aplicação pronta

#### Parte 2: Ambiente Virtual (30 min)
- O que é ambiente virtual e por quê usar?
- Criando ambiente virtual
- Ativando/desativando
- Instalando bibliotecas com pip
- Arquivo requirements.txt

#### Parte 3: Primeiro App Streamlit (45 min)
- Hello World no Streamlit
- Componentes básicos (text, input, button)
- Executando a aplicação
- Hot reload (atualização automática)

#### Parte 4: Hands-on (15 min)
- Alunos criam primeiro app
- Experimentam componentes básicos
- Tiram dúvidas

---

### **AULA 2: Construindo a Aplicação (2h)**

#### Parte 1: Revisão e Estrutura (15 min)
- Revisão da aula anterior
- Apresentação da estrutura do projeto
- Explicação dos arquivos

#### Parte 2: Integração com Banco de Dados (30 min)
- Reutilizando a classe Database
- Inicialização com @st.cache_resource
- Primeiro CRUD: Adicionar filme

#### Parte 3: Interface Completa (45 min)
- Criando abas (tabs)
- Implementando listagem
- Implementando atualização
- Implementando exclusão

#### Parte 4: Melhorias (30 min)
- Validações
- Mensagens de feedback
- Formatação de dados
- Estatísticas

---

### **AULA 3: Prática e Exercícios (2h)**

#### Parte 1: Funcionalidades Extras (45 min)
- Filtros e busca
- Ordenação
- Exportação CSV
- Gráficos básicos

#### Parte 2: Exercícios Guiados (45 min)
- Alunos implementam exercícios básicos
- Professor circula e auxilia
- Discussão de soluções

#### Parte 3: Projeto Livre (30 min)
- Alunos personalizam a aplicação
- Adicionam funcionalidades próprias
- Apresentação rápida dos trabalhos

---

## 🎬 Script de Demonstração Inicial

### Roteiro para apresentar o Streamlit aos alunos:

```
1. "Vamos ver o que vocês vão criar hoje!"
2. Executar: streamlit run app.py
3. Mostrar interface completa funcionando
4. Adicionar um filme
5. Listar e ver estatísticas
6. Atualizar um filme
7. Deletar um filme
8. "Tudo isso foi feito com Python puro, sem HTML ou CSS!"
```

---

## 💡 Dicas Didáticas

### Para Manter o Engajamento:

1. **Compare constantemente** com o módulo console:
   - "Lembram que fazíamos input()? Agora é st.text_input()!"
   - "No lugar de print(), usamos st.write()!"

2. **Mostre resultados rápidos**:
   - Comece com um Hello World
   - Cada conceito novo = resultado visual imediato

3. **Incentive experimentação**:
   - "Tentem mudar a cor!"
   - "E se colocarmos um emoji aqui?"
   - "Que tal adicionar mais um campo?"

4. **Use analogias**:
   - Ambiente virtual = "gaveta organizada só para este projeto"
   - Streamlit = "construir interface como montar Lego"
   - Hot reload = "preview ao vivo enquanto você escreve"

---

## 🔧 Configuração da Sala

### Preparação Prévia:

- [ ] Verificar Python instalado em todas as máquinas
- [ ] Testar criação de venv em uma máquina
- [ ] Verificar internet para download de bibliotecas
- [ ] Preparar repositório com código completo
- [ ] Ter pendrive com instaladores de backup

### Para Cada Aluno:

- [ ] Editor de código (VS Code recomendado)
- [ ] Terminal/Prompt
- [ ] Navegador web
- [ ] Pasta do projeto estruturada

---

## 🐛 Problemas Comuns e Soluções

### 1. Ambiente virtual não ativa
```
Sintoma: "comando python não encontrado" ou "pip não reconhecido"
Solução: Verificar se (venv) aparece no terminal
         Reativar: source venv/bin/activate (Mac/Linux)
                  venv\Scripts\activate (Windows)
```

### 2. Erro ao instalar Streamlit
```
Sintoma: "pip: command not found" ou erro de permissão
Solução: Usar python -m pip install streamlit
         No Windows: executar como administrador
```

### 3. Página em branco no navegador
```
Sintoma: Streamlit inicia mas página não carrega
Solução: Verificar firewall
         Tentar localhost:8501 e 127.0.0.1:8501
         Desabilitar VPN temporariamente
```

### 4. Código não atualiza na tela
```
Sintoma: Alterações no código não aparecem
Solução: Clicar "Always rerun" no canto superior direito
         Ou pressionar R no navegador
```

### 5. Erro "Address already in use"
```
Sintoma: Porta 8501 já está em uso
Solução: streamlit run app.py --server.port 8502
         Ou fechar outros processos Streamlit
```

---

## ✅ Checklist de Avaliação

### Critérios de Avaliação:

**Básico (60%):**
- [ ] Ambiente virtual criado e funcionando
- [ ] Streamlit instalado corretamente
- [ ] Aplicação executa sem erros
- [ ] Consegue adicionar filmes
- [ ] Consegue listar filmes

**Intermediário (80%):**
- [ ] Todas as operações CRUD funcionam
- [ ] Validações implementadas
- [ ] Interface organizada com abas
- [ ] Mensagens de feedback apropriadas
- [ ] Código limpo e comentado

**Avançado (100%):**
- [ ] Funcionalidades extras implementadas
- [ ] Personalização da interface
- [ ] Tratamento de erros robusto
- [ ] Código bem estruturado
- [ ] Exercícios extras completados

---

## 📝 Atividades Avaliativas

### Atividade 1: Setup e Hello World (20 pontos)
- Criar ambiente virtual
- Instalar Streamlit
- Criar app.py com título e texto
- Executar com sucesso

### Atividade 2: Aplicação Básica (40 pontos)
- Implementar adição de filmes
- Implementar listagem
- Interface funcional
- Validações básicas

### Atividade 3: CRUD Completo (40 pontos)
- Atualização funcionando
- Exclusão funcionando
- Feedback adequado
- Tratamento de erros

### Projeto Extra (Bônus): +20 pontos
- Implementar 3 exercícios do EXERCICIOS.md
- Adicionar funcionalidade criativa
- Personalização avançada

---

## 📖 Material Complementar

### Para Distribuir aos Alunos:
- README.md completo
- INICIO-RAPIDO.md
- EXERCICIOS.md
- Código completo comentado
- Links para documentação

### Leitura Recomendada:
- [Documentação oficial Streamlit](https://docs.streamlit.io/)
- [30 Days of Streamlit](https://30days.streamlit.app/)
- [Streamlit Cheat Sheet](https://cheat-sheet.streamlit.app/)

---

## 🎯 Próxima Aula (Preview)

No **Módulo 4**, vocês vão aprender:
- SQLAlchemy ORM
- Trabalhar com banco sem escrever SQL
- Definir modelos como classes Python
- Relacionamentos entre tabelas
- Migrações de banco de dados

---

## 💭 Reflexões Finais

### Perguntas para Discussão:
1. Qual a principal vantagem de usar Streamlit ao invés de console?
2. Quando você usaria uma aplicação web vs. uma aplicação desktop?
3. Como você poderia melhorar a experiência do usuário?
4. Que outras funcionalidades você adicionaria?

### Para Casa:
- Completar exercícios básicos (1-5)
- Pensar em um projeto pessoal usando Streamlit
- Explorar a galeria de exemplos do Streamlit

---

## 📊 Tempo Estimado por Tópico

| Tópico | Tempo |
|--------|-------|
| Introdução e motivação | 30 min |
| Ambiente virtual | 45 min |
| Primeiro app Streamlit | 45 min |
| Integração com banco | 45 min |
| CRUD completo | 90 min |
| Melhorias e validações | 45 min |
| Exercícios práticos | 60 min |
| **TOTAL** | **5h 30min** |

---

## 🎉 Dicas para Finalizar a Aula

1. **Recapitular conquistas:**
   - "Olhem o quanto vocês aprenderam!"
   - "Saíram de console para web em algumas horas!"

2. **Encorajar continuidade:**
   - "Explorem os exercícios em casa"
   - "Compartilhem seus projetos no grupo"

3. **Preview da próxima aula:**
   - "Na próxima, vamos deixar ainda mais profissional!"
   - "Vão adorar o SQLAlchemy!"

4. **Feedback:**
   - "O que acharam mais legal?"
   - "O que foi mais desafiador?"

---

**Boa aula! 🚀**
