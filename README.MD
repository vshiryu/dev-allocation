# Dev Allocation

## Pré-requisitos

Certifique-se de ter os seguintes programas instalados:

- Docker
- Docker Compose
- Python 3.10 ou superior

## Passos para Rodar a API

1. Clone o Repositório

Clone o repositório do projeto para sua máquina local.
Abra o terminal na pasta do repositório.

2. Crie um arquivo `.env` na raiz do projeto

Você pode apenas copiar e colar o conteúdo de .env.example para o .env

DEBUG=True
SECRET_KEY=dwaniodqa2n0229h0e
DATABASE_URL=postgres://developer:developerpassword@db:5432/dev_allocation
DB_NAME=dev_allocation
DB_USER=developer
DB_PASSWORD=developerpassword
DB_HOST=db
DB_PORT=5432

3. Subindo os Containers (API e Postgres):

docker-compose up --build
ou
docker compose up --build

4. Acesse a API

A API estará rodando na URL http://localhost:8000/.

5. Testando a API com Swagger

Swagger na seguinte URL:

http://localhost:8000/api/schema/swagger-ui/

