# 🚀 Início Rápido - Sistema de Filmes com Streamlit

Este guia rápido irá ajudá-lo a executar o sistema em menos de 5 minutos!

## ⚡ Passos Rápidos

### 1. Navegue até a pasta do projeto
```bash
cd 3-app-web
```

### 2. Crie o ambiente virtual
```bash
# macOS/Linux
python3 -m venv venv

# Windows
python -m venv venv
```

### 3. Ative o ambiente virtual
```bash
# macOS/Linux
source venv/bin/activate

# Windows (CMD)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1
```

### 4. Instale as dependências
```bash
pip install -r requirements.txt
```

### 5. Execute a aplicação
```bash
streamlit run app.py
```

### 6. Acesse no navegador
O Streamlit abrirá automaticamente, ou acesse: **http://localhost:8501**

---

## ✅ Verificação

Se tudo funcionou, você verá:
- ✅ Tela com título "🎬 Sistema de Gerenciamento de Filmes"
- ✅ Quatro abas: Adicionar, Listar, Atualizar, Deletar
- ✅ Interface moderna e responsiva

---

## 🛑 Problemas Comuns

### "streamlit: command not found"
**Solução:** Certifique-se de que o ambiente virtual está ativado. Você deve ver `(venv)` no terminal.

### "No module named 'streamlit'"
**Solução:** Instale novamente com `pip install streamlit`

### A página não abre
**Solução:** Verifique se a porta 8501 não está em uso. Tente outra porta:
```bash
streamlit run app.py --server.port 8502
```

---

## 🎯 Próximos Passos

1. **Adicione alguns filmes** usando a primeira aba
2. **Explore as funcionalidades** de listar, atualizar e deletar
3. **Leia o README.md completo** para entender cada conceito
4. **Faça os exercícios** do arquivo EXERCICIOS.md

---

## 📚 Arquivos do Projeto

- `app.py` - Aplicação Streamlit principal
- `models.py` - Classe Database para gerenciar o SQLite
- `requirements.txt` - Dependências do projeto
- `README.md` - Documentação completa
- `EXERCICIOS.md` - Lista de exercícios práticos

---

**Divirta-se aprendendo! 🎉**
