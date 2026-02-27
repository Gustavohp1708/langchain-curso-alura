
# langchain-curso-alura

Projeto exemplo do curso usando LangChain.

**Descrição:**
- Exemplo simples com `agente.py` e `main.py` que demonstra integração com LangChain.

**Requisitos**
- Python 3.10+ (ou versão compatível)
- Ambiente virtual recomendado

**Gerenciamento de dependências**
- Este projeto usa o gerenciador `uv` (não há `requirements.txt`).
- Para instalar dependências (exemplo):

PowerShell:

```powershell
python -m venv .venv
& .venv\Scripts\Activate.ps1
uv add langchain langchain-groq
```

Linux / macOS (exemplo):

```bash
python -m venv .venv
source .venv/bin/activate
uv add langchain langchain-groq
```

**Executando o projeto**
- Ative o ambiente virtual e execute:

```powershell
& .venv\Scripts\python.exe agente.py
# ou
& .venv\Scripts\python.exe main.py
```

**Git / GitHub**
- Repositório remoto: https://github.com/Gustavohp1708/langchain-curso-alura
- Faça commits das suas alterações e `push` para o branch `main`.

Se quiser, posso também gerar instruções adicionais (ex.: `README` com exemplos de uso, badges ou arquivo de licença).

