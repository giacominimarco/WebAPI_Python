# Instruções de configuração e execução

1. Efetuar o clone do projeto;
2. Acessar a parta WebAPI_Python;
3. Dentro da pasta WebAPI_Python, rodar o comando para criação de uma venv que será responsavel por alocar as dependencias do projeto:
   ```
     python -m venv venv
   ```
4. Para ativar a venv:

    | Plataforma  | Shell           | Comando para ativar o ambiente virtual |
    | :---:       | :---:           |  :---                                  |
    | POSIX       | bash/zsh        | `$ source <venv>/bin/activate`         |
    | POSIX       | fish            | `$ source <venv>/bin/activate.fish`    |
    | POSIX       | csh/tcsh        | `$ source <venv>/bin/activate.csh`     |
    | POSIX       | PowerShell      | `$ <venv>/bin/Activate.ps1`            |
    | Windows     | cmd.exe         | `C:\> <venv>\Scripts\activate.bat`     |
    | Windows     | PowerShell      | `PS C:\> <venv>\Scripts\Activate.ps1`  |
5. Para instalar todos os pacotes necessários para o ambiente:
   ```
     pip install -r requirements.txt
   ```
6. Para rodar o projeto:
   ```
     python manager.py runserver
   ```
7. Para acessar o login do sistema: **http://127.0.0.1:8000/auth/login**.
   
# WebAPI_Python

Desafio:

Crie uma API para criação, listagem e login de usuários utilizando Python e SQLite. Desenvolva também uma interface front-end simples. Hospede o código em um repositório público no GitHub.

Instruções:

Funcionalidades da API:
- Criar Usuário: Endpoint para criar um novo usuário (usuário, senha).
- Listar Usuários: Endpoint para listar todos os usuários.
- Login de Usuário: Endpoint para realizar login (usuário, senha).

Interface Front-End:
- Página de Cadastro: Formulário para criar um novo usuário.
- Página de Login: Formulário para login do usuário.
- Página de Listagem: Visualização de todos os usuários cadastrados.
