<div align="center">
  <h1>🔐 User Authentication System</h1>
  <p><i>Sistema de autenticação web com Flask, frontend server-side e banco SQLite local</i></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Flask-3.1-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
    <img src="https://img.shields.io/badge/SQLite-Local-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
    <img src="https://img.shields.io/badge/Jinja2-Templates-B41717?style=for-the-badge&logo=jinja&logoColor=white" alt="Jinja2" />
    <img src="https://img.shields.io/badge/CSS-UI-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS" />
  </p>
</div>

---

## ⚡ Visão Geral

O **User Authentication System** é uma aplicação web para cadastro e login de usuários com persistência local em SQLite.

O projeto aplica uma arquitetura organizada em camadas, separando responsabilidades de **rotas**, **serviços de autenticação**, **acesso a banco de dados** e **interface frontend** com templates.

## ✨ Principais Recursos

- **Cadastro de usuários com validação**:
  - Validação de campos obrigatórios, CPF e confirmação de senha.
  - Verificação de unicidade para `username` e `cpf`.
- **Login seguro**:
  - Autenticação com senha hasheada via `werkzeug.security`.
  - Sessão de usuário para controle de acesso.
- **Dashboard protegido**:
  - Página acessível apenas para usuários autenticados.
- **Logout com limpeza de sessão**:
  - Encerramento seguro da autenticação no navegador.
- **Banco local automático**:
  - Criação da tabela `users` automaticamente ao iniciar a aplicação.

## 🛠️ Stack Tecnológica

- **Backend**: Flask 3.1
- **Frontend**: Jinja2 + HTML + CSS
- **Banco de Dados**: SQLite (arquivo local em `instance/auth.db`)
- **Segurança de Senha**: Werkzeug (`generate_password_hash` / `check_password_hash`)
- **Gerenciamento de Dependências**: Poetry (`pyproject.toml`)

## 📂 Estrutura do Projeto

```text
.
├── app/
│   ├── routes/
│   │   ├── __init__.py
│   │   └── auth.py              # Rotas web (index, register, login, dashboard, logout)
│   ├── services/
│   │   ├── __init__.py
│   │   └── auth_service.py      # Regras de negócio da autenticação
│   ├── static/
│   │   └── css/
│   │       └── style.css        # Estilos da aplicação
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── register.html
│   │   ├── login.html
│   │   └── dashboard.html
│   ├── __init__.py              # App factory Flask
│   └── db.py                    # Conexão SQLite, init e queries utilitárias
├── instance/
│   └── auth.db                  # Banco local (gerado automaticamente)
├── main.py                      # Entrypoint principal
├── run.py                       # Entrypoint alternativo
├── pyproject.toml
├── poetry.lock
└── README.md
```

## 🚀 Como Rodar Localmente

### Pré-requisitos

- Python 3.10+

### Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/NullCipherr/User_Authentication_System.git
   cd User_Authentication_System
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install Flask
   ```

4. Inicie a aplicação:
   ```bash
   python main.py
   ```

5. Acesse no navegador:
   - `http://127.0.0.1:5000`

## 📜 Rotas Disponíveis

- `GET /`: página inicial
- `GET /register`: formulário de cadastro
- `POST /register`: criação de usuário
- `GET /login`: formulário de login
- `POST /login`: autenticação de usuário
- `GET /dashboard`: área protegida
- `POST /logout`: logout da sessão

## 🔐 Segurança

- Senhas **não são salvas em texto puro**.
- O projeto utiliza hash de senha com Werkzeug.
- Sessões Flask são usadas para controle de autenticação.

## 🔄 Melhorias Futuras

- Adicionar testes automatizados (unitários e integração).
- Implementar CSRF token nos formulários.
- Criar recuperação de senha e confirmação de e-mail.
- Incluir migrações de banco (ex: Alembic/Flask-Migrate).

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---

<div align="center">
  <p>Desenvolvido por <a href="https://github.com/NullCipherr">NullCipherr</a></p>
</div>
