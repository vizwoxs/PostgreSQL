# CRUD COM POSTGRESQL + PYTHON

Este projeto é um exemplo prático de CRUD usando:
- Banco de dados  **PostgreSQL**
- Conexão com **psycopg2**
- Interface web com **Streamlit**

## Como executar

### 1. Clonar o repositório
```bash
https://github.com/vizwoxs/PostgreSQL.git
```

### 2. Criar ambiente virtual (opcinal)
```bash
python -m venv .venv
.venv\Scripts\activate #windows
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente
crie um arquivo .env na raiz do projeto com:

DB_NAME=nome_banco

DB_USER=postgres

DB_PASSWORD=sua_senha

DB_HOST=localhost

DB_PORT=5432

### 5. Rodar aplicação
```bash
python -m streamlit run app.py
```

### Funcionalidades

- Conexão com o banco
- Criar alunos
- Listar alunos
- Atualizar alunos
- Deletar alunos

### Autor
Projeto desenvolvido em aulapara treinar python + postgresql
Professor: Gabriel Brito de sousa
