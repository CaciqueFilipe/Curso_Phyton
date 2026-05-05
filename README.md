# Curso de Python
Curso de Python com Gustavo Guanabara

Repositório dedicado aos exercícios e aulas do curso de Python.

## 🛠️ Configuração do Ambiente

Como este projeto utiliza Python 3.12+ no Ubuntu, é necessário utilizar um ambiente virtual para instalar dependências externas (conforme o PEP 668).

### Passo a passo para preparar o ambiente:

1. **Criar o ambiente virtual:**
   ```bash
   python3 -m venv .venv
   ```

2. **Ativar o ambiente:**
   ```bash
   source .venv/bin/activate
   ```

3. **Instalar as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

### 🛠️ Configuração no VS Code
Para que o VS Code reconheça as bibliotecas instaladas no `.venv`:
1. Pressione `Ctrl + Shift + P`.
2. Digite **Python: Select Interpreter**.
3. Selecione o interpretador que está dentro da pasta `.venv`.

## 🚀 Como executar

Após ativar o ambiente virtual, você pode executar os desafios ou aulas:
```bash
python3 aulas/004_Modulos_4.py
```