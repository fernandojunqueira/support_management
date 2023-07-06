# support_management

A Rest API de controlador de chamadas é uma solução de back-end desenvolvida em Python Flask. Com essa API, é possível criar, atualizar, visualizar e excluir chamadas, bem como controlar o status e ações das chamadas em andamento.

## Instalação

Para inciar este projeto, é necessário instalar as dependências. Para fazer a instalação basta dar o seguinte comando:

```
pip install -r requirements.txt
```

## Uso Local

1. Seguindo o modelo do arquivo .env.example., crie um arquivo chamado .env e configure as informações de acesso.

2. Execute as migrations do banco de dados:

```bash
flask db init
flask db migrate
flask db upgrade
```

3. Inicie o servidor, para isso para pasta flaskr e rode o comando:

```bash
flask run
```

4. As rotas podem ser acessadas pelo endereço:

```bash
http://localhost:5000
```

## Rotas

# customer
    - POST "/customer/register" - responsável pela criação do usuário.
        - body = {
	        "username": "Fernando",
	        "email": "fernando@mail.com",
	        "phone": "48999999999",
	        "address": "address",
	        "password": "1234"
            }
        - response = {
	        "address": "address",
	        "email": "fernando@mail.com",
	        "id": 1,
	        "phone": "48999999999",
	        "username": "Fernando"
            }
    - GET "/customer/<int:customer_id>" - responsável pela leitura do usuário.
    - DELETE "/customer/<int:customer_id>" - responsável pela deleção do usuário

# login
    - POST "/login" - responsável por fazer o login e retornar o token
        - body = {
	        "email": "fernando@mail.com",
	        "password": "1234"
        }
        - response = {
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lcl9pZCI6MSwiZW1haWwiOiJmZXJuYW5kb0BtYWlsLmNvbSJ9.riIj5hdfPL-X3Tniq4c4iqZP094hNMvamAN3ct2zUAE"
        }

# ticket - Rotas protegidas por Bearer token
    - POST "/ticket/<customer_id>" - responsável pela criação da requisição de chamado.
        - body = {
	        "title": "Example",
	        "description": "example"
        }  
        - response = {
	        "customer": {
	        	"address": "address",
	        	"email": "fernando@mail.com",
	        	"phone": "48999999999"
	        },
	        "description": "Example",
	        "id": 1,
	        "status": "open",
	        "title": "Example"
        }
    - PATCH "/ticket/<int:ticket_id>" - responsável pela atualização do chamado. Pode alterar o status, title e description.
        - body = {
	        "title": "Example",
	        "description": "example",
            "status": "closed"
        }  
        - response = {
	        "customer": {
	        	"address": "address",
	        	"email": "fernando@mail.com",
	        	"phone": "48999999999"
	        },
	        "description": "Example",
	        "id": 1,
	        "status": "closed",
	        "title": "Example"
        }
    - DELETE "/ticket/<int:ticket_id>" - responsável pela deleção do chamado.
    - GET "/ticket" - responsável pela listagem dos chamados.
        - response = [
	        {
	        	"customer": {
	        		"address": "address",
	        		"email": "fernando@mail.com",
	        		"phone": "48999999999"
	        	},
	        	"description": "Example",
	        	"id": 1,
	        	"status": "closed",
	        	"title": "Example"
	        }
        ]

## Testes

Essa aplicação possui testes unitários. Para rodar os testes é preciso estár no diretório support_management e rodar o seguinte comando:

```bash
 pytest tests/
```

