# VagasTrack

O **VagasTrack** é uma aplicação web criada para ajudar usuários a **organizar e acompanhar candidaturas a vagas de emprego**.

O sistema permite que usuários se cadastrem, façam login e gerenciem suas próprias candidaturas através de um painel simples e intuitivo.

Além disso, o projeto conta com um **painel administrativo**, onde o administrador pode visualizar os usuários cadastrados e gerenciar suas informações.

Este projeto foi desenvolvido como **projeto de portfólio**, com foco em praticar conceitos importantes de desenvolvimento backend, como autenticação, manipulação de banco de dados e operações CRUD.

---

# Funcionalidades

- Cadastro de usuários  
- Sistema de login com sessão  
- CRUD completo de vagas  
  - Criar vaga  
  - Visualizar vagas  
  - Editar vaga  
  - Deletar vaga  
- Cada usuário visualiza **apenas suas próprias vagas**  
- Painel administrativo  
- Admin pode visualizar usuários e suas vagas  
- Proteção para impedir a exclusão do usuário administrador  

---

# Tecnologias Utilizadas

## Backend
- Python
- FastAPI
- SQLAlchemy

## Frontend
- HTML
- CSS
- JavaScript
- Jinja2 Templates

## Banco de Dados
- SQLite

---

# Estrutura do Projeto
app/
│
├── models/ # Modelos do banco de dados
├── services/ # Lógica de negócio
├── routes/ # Rotas da aplicação
├── templates/ # Páginas HTML
├── static/ # Arquivos CSS e JavaScript
│
└── main.py # Arquivo principal da aplicação
---

# Como Executar o Projeto

### 1. Clonar o repositório
git clone https://github.com/EnzoSanchez23/VagasTrack.git

### 2. Entrar na pasta do projeto
cd VagasTrack


### 3. Criar ambiente virtual
python -m venv venv


### 4. Ativar o ambiente virtual

Windows:
venv\Scripts\activate


### 5. Instalar dependências
pip install -r requirements.txt


### 6. Executar a aplicação
uvicorn app.main:app --reload
A aplicação estará disponível em: http://127.0.0.1:8000


---

# Melhorias Futuras

Algumas melhorias planejadas para evoluções futuras do projeto:

- Implementação de **hash de senha (bcrypt)**
- Validação de dados com **Pydantic**
- Melhorias na interface do usuário

---

# Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de praticar:

- Desenvolvimento backend com FastAPI
- Autenticação e controle de sessão
- Operações CRUD
- Relacionamento entre tabelas no banco de dados
- Organização de código em camadas (routes, services, models)

---

# Autor

**Enzo Sanchez**

GitHub:  
https://github.com/EnzoSanchez23
