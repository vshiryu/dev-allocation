# Dev Allocation

## Pré-requisitos

Certifique-se de ter os seguintes programas instalados:

- Docker
- Docker Compose

## Passos para Rodar a API

1. Clone o Repositório

Clone o repositório do projeto para sua máquina local.
Abra o terminal na pasta do repositório.

2. Crie um arquivo `.env` na raiz do projeto
Você pode apenas copiar e colar o conteúdo de .env.example para o .env:
```bash
cp .env.example .env
```

3. Subindo os Containers (API e Postgres):
```bash
docker-compose up --build
```
ou
```bash
docker compose up --build
```

4. Acesse a API

A API estará rodando na URL http://localhost:8000/.

5. Testando a API com Swagger

Swagger na URL:

http://localhost:8000/api/schema/swagger-ui/

