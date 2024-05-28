# WebTrap - Django Honeypot

WebTrap é um projeto Django que implementa um formulário honeypot. O honeypot é uma armadilha para detectar e registrar atividades suspeitas, como acessos não autorizados e preenchimento automatizado de formulários.

## Funcionalidades

- Formulário de captura de dados (nome e e-mail).
- Detecção de acesso ao honeypot.
- Registro de atividades suspeitas.
- Página de aviso quando a armadilha é acionada.

## Tecnologias Utilizadas

- Python 3.12
- Django 5.0.6
- SQLite (banco de dados)
- HTML/CSS (templates)
    
    ## Iniciando o projeto
    
    ## clone o repositório
    
    git clone [https://github.com/seu-usuario/WebTrap.git](https://github.com/seu-usuario/WebTrap.git) cd WebTrap

## crie um ambiente virtual

python -m venv venv source venv/bin/activate # Para Linux/Mac venv\Scripts\activate # Para Windows

## instale as dependências

pip install django

## execute as migrações

python manage.py migrate

## inicie o servidor de desenvolvimento

python manage.py runserver

## acesse o projeto no navegador

[http://127.0.0.1:8000/webtrap/honeypot-form/](http://127.0.0.1:8000/webtrap/honeypot-form/)

## Como Funciona

Acesse o formulário honeypot em /webtrap/honeypot-form/. Preencha o formulário e envie. Se a armadilha for acionada, uma mensagem de aviso será exibida e a atividade será registrada no banco de dados.
