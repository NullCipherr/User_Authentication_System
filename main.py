import secrets
import os


def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')


# Função para verificar se a senha está correta de forma segura
def is_password_correct(input_password, hashed_password):
  return secrets.compare_digest(input_password, hashed_password)


# Definindo a senha hasheada
def define_hashed_password(password):
  hashed_password = secrets.token_hex(16)  # Gera uma senha hasheada aleatória
  return hashed_password


class User:
  # Função de inicialização do usuário.
  def __init__(self, name, cpf, username, password):
    self.name = name
    self.cpf = cpf
    self.username = username
    self.password = password

  # Função para exibir as informações do usuário.
  def show_user(self):
    print('Informações sobre o usuario')
    print(f'Name: {self.name}')
    print(f'CPF: {self.cpf}')
    print(f'Username: {self.username}')
    print(f'Password: {self.password}')


# Função para registrar um novo usuário
def register_user():
  # Limpa a tela sempre quando iniciado
  clear_console()

  # Dados de usuario.
  name = input('Name: ')
  username = input('Username: ')
  cpf = input('CPF: ')
  password = input('Password: ')
  repeat_pasword = input('Repeat password: ')

  # Verifica se o formulário foi preenchido corretamente.
  if not all([username, cpf, password, repeat_pasword]):
    print('Preencha todos os campos!!')
    register_user()

  # Verifica se o cpf é valido.
  if len(cpf) > 11:
    print('CPF invalido..')
    register_user()

  # Verifica se a senha é valida.
  if len(password) < 6:
    print('Senha invalida..')
    register_user()

  # Verifica se a senha é igual a senha reptidida.
  if password != repeat_pasword:
    print('As senhas não são iguais!!')
    register_user()

  hashed_password = define_hashed_password(password)

  # Cria um objeto User com os dados preenchidos.
  user = User(name, username, cpf, hashed_password)

  # Retorna o objeto User.
  return user


# Função de login do usuário.
def login_user(users):
  # Limpa a tela sempre quando iniciado
  clear_console()

  # Dados de entrada do usuario.
  input_username = input('Username: ')
  input_password = input('Password: ')

  hashed_password = define_hashed_password(input_password)

  # Verifica se o formulário foi preenchido corretamente.
  if not all([input_username, input_password]):
    print('Preencha todos os campos corretamente!!')
    login_user(users)

  # Verifica se o usuário existe.
  found_user = None
  for user in users:
    if input_username == user.username:
      found_user = user
      break

    if not found_user:
      print('Usuário não existe!!')
      login_user(users)

  # Verifica se a senha está correta.
  if is_password_correct(input_password, hashed_password):
    print('Senha correta!')
  else:
    print('Senha incorreta!')


def __main__():
  # Cria uma lista de usuários.
  users = []
  # Registra um novo usuário.
  user = register_user()
  # Adiciona o usuário à lista de usuários.
  users.append(user)
  # Faz o login do usuário.
  login_user(users)
