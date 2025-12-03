# 🏠 Atividade para Casa 1 - Meu Primeiro App Streamlit

## 📋 Informações da Atividade

**Objetivo:** Praticar os componentes básicos do Streamlit criando um formulário de cadastro
**Consulta da Documentação:** https://docs.streamlit.io/develop/api-reference
---

## 🎯 Objetivo

Criar uma aplicação Streamlit simples que simula um **formulário de cadastro pessoal**. 

---

## 📝 O que você deve fazer

Crie um arquivo chamado `meu_cadastro.py` com um formulário que coleta as seguintes informações:

### Dados Obrigatórios:

1. **Nome completo** (text_input)
2. **Idade** (number_input)
3. **E-mail** (text_input)
4. **Cidade** (text_input)
5. **Cor favorita** (selectbox com opções: Azul, Verde, Vermelho, Amarelo, Roxo)
6. **Hobbies** (multiselect com opções: Esportes, Música, Leitura, Jogos, Arte, Culinária)
7. **Aceita receber novidades** (checkbox)

### Funcionalidades Obrigatórias:

1. Um **botão** "Enviar Cadastro"
2. Mostrar uma **mensagem de sucesso** quando o formulário for enviado
3. Usar **título** e **subtítulos** para organizar a página

---

## 🌟 Desafios Extras (Opcional)

Se quiser ir além, tente adicionar:

1. **Validação básica (+0.5)**: Não permitir enviar se o nome estiver vazio
   ```python
   if nome.strip() == "":
       st.error("❌ O nome não pode estar vazio!")
   ```

2. **Campo de senha (+0.5)**: Adicione um campo de senha usando `st.text_input("Senha", type="password")`

3. **Efeito visual (+0.5)**: Use `st.balloons()` quando o cadastro for enviado com sucesso

---

## 📚 Componentes que Você Vai Usar

Revise estes componentes antes de começar:

| Componente | Para que serve | Exemplo |
|------------|----------------|---------|
| `st.title()` | Título principal | `st.title("Meu App")` |
| `st.subheader()` | Subtítulo | `st.subheader("Seção 1")` |
| `st.text_input()` | Campo de texto | `nome = st.text_input("Nome")` |
| `st.number_input()` | Campo numérico | `idade = st.number_input("Idade")` |
| `st.selectbox()` | Menu dropdown | `cor = st.selectbox("Cor", ["Azul", "Verde"])` |
| `st.multiselect()` | Seleção múltipla | `hobbies = st.multiselect("Hobbies", ["A", "B"])` |
| `st.checkbox()` | Caixa de seleção | `aceito = st.checkbox("Aceito")` |
| `st.button()` | Botão clicável | `if st.button("Enviar"):` |
| `st.success()` | Mensagem de sucesso | `st.success("Sucesso!")` |
| `st.error()` | Mensagem de erro | `st.error("Erro!")` |
| `st.write()` | Exibir texto/dados | `st.write("Texto")` |
| `st.markdown()` | Texto formatado | `st.markdown("---")` |

---

## 🚀 Como Executar

1. Crie o arquivo `meu_cadastro.py` na pasta do projeto
2. Escreva seu código
3. No terminal, execute:
   ```bash
   streamlit run meu_cadastro.py
   ```
4. A aplicação abrirá no navegador automaticamente

---

## 💡 Dicas Importantes

1. **Salve o arquivo** antes de executar
2. **Leia as mensagens de erro** - elas ajudam a encontrar problemas

---

## 🐛 Problemas Comuns

### Erro: "No module named 'streamlit'"
**Solução:** Certifique-se de que o ambiente virtual está ativado e o Streamlit instalado
```bash
source venv/bin/activate  # Mac/Linux
.\venv\Scripts\activate  # Windows
pip install streamlit
```

### Código não funciona
**Solução:** Verifique a indentação - Python é sensível a espaços!

---

## 📤 Como Entregar

1. Salve seu arquivo `meu_cadastro.py`
2. Tire um **print/screenshot** da aplicação funcionando
3. Envie o arquivo `.py` e a imagem conforme instruções do professor

---

## 📖 Referências Úteis

- [Documentação Streamlit - Inputs](https://docs.streamlit.io/library/api-reference/widgets)
- [Documentação Streamlit - Text](https://docs.streamlit.io/library/api-reference/text)
- [Cheat Sheet Streamlit](https://cheat-sheet.streamlit.app/)
