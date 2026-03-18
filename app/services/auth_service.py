from werkzeug.security import check_password_hash, generate_password_hash

from app.db import execute, fetch_one


def validate_registration_form(
    name: str,
    cpf: str,
    username: str,
    password: str,
    repeat_password: str,
) -> str | None:
    if not all([name, cpf, username, password, repeat_password]):
        return "Preencha todos os campos."

    if len(cpf) != 11 or not cpf.isdigit():
        return "CPF inválido. Use 11 dígitos numéricos."

    if len(password) < 6:
        return "Senha inválida. Use ao menos 6 caracteres."

    if password != repeat_password:
        return "As senhas não conferem."

    if fetch_one("SELECT id FROM users WHERE username = ?", (username,)):
        return "Username já está em uso."

    if fetch_one("SELECT id FROM users WHERE cpf = ?", (cpf,)):
        return "CPF já cadastrado."

    return None


def register_user(name: str, cpf: str, username: str, password: str) -> int:
    password_hash = generate_password_hash(password)
    return execute(
        "INSERT INTO users (name, cpf, username, password_hash) VALUES (?, ?, ?, ?)",
        (name, cpf, username, password_hash),
    )


def authenticate_user(username: str, password: str):
    user = fetch_one("SELECT * FROM users WHERE username = ?", (username,))
    if not user:
        return None

    if not check_password_hash(user["password_hash"], password):
        return None

    return user
