# BJJEventOS - API REST para Gerenciamento de Campeonatos de Jiu-Jitsu

Plataforma RESTful especializada na gestao de torneios de Jiu-Jitsu (padrao IBJJF/CBJJ), desenvolvida por Maria Luiza em Python 3.12, FastAPI, SQLAlchemy e PostgreSQL / SQLite.

## Perfis de Acesso e Matriz RBAC
- Admin (admin): Controle global do sistema, credenciamento de organizadores, visualizacao irrestrita de usuarios e exclusao de eventos.
- Organizador (organizador): Cadastro de torneios, definicao de tatames, encerramento da checagem geral, geracao de chaves de luta e lancamento de placares.
- Atleta (atleta): Gestao da propria ficha biometrica (Faixa, Peso, Idade, Academia/Equipe), consulta de eventos, inscricao por categoria (Peso e Absoluto) e acompanhamento de chaves.

## Matriz de Permissoes e Protecao de Endpoints

- POST /api/v1/usuarios (Publico)
- POST /api/v1/auth/login (Publico)
- GET /api/v1/usuarios/me (Autenticado: admin, organizador, atleta -> 401 se sem token)
- GET /api/v1/usuarios (Exclusivo admin -> 401 se sem token, 403 se perfil incompativel)
- POST /api/v1/atleta/perfil (Exclusivo atleta -> 401 se sem token, 403 se perfil incompativel)
- PUT /api/v1/atleta/perfil (Exclusivo atleta -> 401 se sem token, 403 se perfil incompativel)
- POST /api/v1/eventos (Organizador / Admin -> 401 se sem token, 403 se perfil incompativel)
- POST /api/v1/eventos/{id}/categorias (Organizador / Admin -> 401 se sem token, 403 se perfil incompativel)
- POST /api/v1/inscricoes (Exclusivo atleta -> 401 se sem token, 403 se perfil incompativel)
- PUT /api/v1/lutas/{id}/resultado (Organizador / Admin -> 401 se sem token, 403 se perfil incompativel)

## Credenciais dos Perfis de Teste (Swagger UI)

- Administrador (admin): admin@bjj.com / adminPassword123
- Organizador (organizador): organizador@bjj.com / orgPassword123
- Atleta Competidor (atleta): atleta@bjj.com / atletaPassword123

## Como Executar a Aplicacao

1. Criar e ativar o ambiente virtual
python3 -m venv venv
source venv/bin/activate

2. Instalar dependencias
pip install -r requirements.txt

3. Configurar variaveis de ambiente
cp .env.example .env

4. Executar o servidor FastAPI
uvicorn app.main:app --reload

Documentacao Interativa:
- Swagger UI: /docs
- ReDoc: /redoc

## Como Executar os Testes Automatizados

python run_tests.py
# ou
pytest -v
