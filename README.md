# BJJEventOS - API REST para Gerenciamento de Campeonatos de Jiu-Jitsu

Plataforma RESTful especializada na gestão de torneios de Jiu-Jitsu (padrão IBJJF/CBJJ), desenvolvida por **Maria Luiza** em **Python 3.12**, **FastAPI**, **SQLAlchemy** e **PostgreSQL / SQLite**.

---

## 🥋 Perfis de Acesso e Matriz RBAC

- **Admin (admin):** Controle global do sistema, credenciamento de organizadores, visualização irrestrita de usuários e exclusão de eventos.
- **Organizador (organizador):** Cadastro de torneios, definição de tatames, encerramento da checagem geral, geração de chaves de luta e lançamento de placares.
- **Atleta (atleta):** Gestão da própria ficha biométrica (Faixa, Peso, Idade, Academia/Equipe), consulta de eventos, inscrição por categoria (Peso e Absoluto) e acompanhamento de chaves.

### Matriz de Permissões e Proteção de Endpoints

| Método e Rota | Quem pode | Sem token | Perfil incompatível |
| --- | --- | --- | --- |
| POST `/api/v1/usuarios` | Público | - | - |
| POST `/api/v1/auth/login` | Público | - | - |
| GET `/api/v1/usuarios/me` | admin, organizador, atleta | 401 | - |
| GET `/api/v1/usuarios` | Exclusivo admin | 401 | 403 |
| POST `/api/v1/atleta/perfil` | Exclusivo atleta | 401 | 403 |
| PUT `/api/v1/atleta/perfil` | Exclusivo atleta | 401 | 403 |
| POST `/api/v1/eventos` | Organizador / Admin | 401 | 403 |
| POST `/api/v1/eventos/{id}/categorias` | Organizador / Admin | 401 | 403 |
| POST `/api/v1/inscricoes` | Exclusivo atleta | 401 | 403 |
| PUT `/api/v1/lutas/{id}/resultado` | Organizador / Admin | 401 | 403 |

### Credenciais dos Perfis de Teste (Swagger UI)

- **Administrador (admin):** admin@bjj.com / adminPassword123
- **Organizador (organizador):** organizador@bjj.com / orgPassword123
- **Atleta Competidor (atleta):** atleta@bjj.com / atletaPassword123

---

## ✨ Funcionalidades

- Cadastro e autenticação de usuários com JWT
- Controle de acesso por perfil (Admin, Organizador, Atleta)
- Cadastro de atletas com faixa, peso, idade e academia
- Criação e gerenciamento de eventos e categorias
- Inscrição de atletas por categoria (Peso e Absoluto)
- Geração de chaves de lutas
- Lançamento de placares e resultados

---

## 🛠️ Tecnologias

- Python 3.12
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic / Pydantic Settings
- Alembic
- PyJWT
- Passlib + Bcrypt
- Python-Multipart
- Pytest + HTTPX
- PostgreSQL / SQLite

---

## ⚙️ Como Executar no seu PC (Windows)

### 1. Criar e ativar o ambiente virtual

```bash
py -m venv venv
.\venv\Scripts\Activate.ps1
### 2. Instalar dependências
py -m pip install -r requirements.txt
### 3. Configurar variáveis de ambiente
copy .env.example .env
Exemplo do arquivo `.env`:
DATABASE_URL=sqlite:///./bjjeventos.db
SECRET_KEY=sua-chave-secreta-aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
Para usar PostgreSQL, troque o `DATABASE_URL` para:
DATABASE_URL=postgresql://usuario:senha@localhost:5432/bjjeventos
### 4. Executar o servidor
py -m uvicorn app.main:app --reload
Acesse:
- API: `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### No Linux / Mac, os comandos mudam só aqui:
python3 -m venv venv
source venv/bin/activate
cp .env.example .env
uvicorn app.main:app --reload
---

## ☁️ Como Executar no GitHub (Codespaces)

O GitHub sozinho não roda a API, quem roda é o *GitHub Codespaces*.

### 1. Abrir o Codespaces

Vá em `github.com/codespaces` e clique em *Open in browser* no seu codespace.
Ou no repositório, clique em *Code > Codespaces > Create codespace on main*.

### 2. Entrar na pasta da API
cd bjjeventos-api
### 3. Instalar as dependências
pip install -r requirements.txt
pip install python-multipart
### 4. Rodar a API no Codespaces

No Codespaces precisa do `--host 0.0.0.0`:
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
### 5. Abrir no navegador

Na aba *PORTAS / PORTS* embaixo, clique na porta `8000` > *Open in Browser*.

Vai abrir um link tipo:
https://humble-sniffle-4qr544vp669g3j4v9-8000.app.github.dev/
Para a documentação, coloque `/docs` no final:
https://humble-sniffle-4qr544vp669g3j4v9-8000.app.github.dev/docs
---

## 💾 Como Salvar e Fechar o Git Corretamente

Não feche a aba sem salvar. Faça nessa ordem:

### 1. Parar a API

Clique no terminal onde o `uvicorn` está rodando e aperte:
Ctrl + C
### 2. Voltar para a pasta principal
cd /workspaces/BJJEventOS
### 3. Ver o que mudou
git status
### 4. Adicionar tudo
git add .
### 5. Salvar com mensagem
git commit -m "Atualiza README e corrige API"
### 6. Enviar para o GitHub
git push origin main
Se aparecer `main -> main`, já subiu com sucesso.

### 7. Desligar o Codespace

Clique embaixo à esquerda em `Codespaces: humble sniffle` > *Stop Current Codespace*.

Ou vá em `github.com/codespaces` > 3 pontinhos > *Stop codespace*.

### Para baixar o projeto em outro PC
git clone https://github.com/MariaLu1725/BJJEventOS.git
cd BJJEventOS/bjjeventos-api
---

## 📡 Principais Endpoints
Método | Rota | Descrição
POST | `/api/v1/auth/login` | Login e geração do token JWT
POST | `/api/v1/usuarios` | Cadastro de novo usuário
GET | `/api/v1/usuarios/me` | Dados do usuário logado
GET | `/api/v1/usuarios` | Listar usuários (Admin)
POST | `/api/v1/atleta/perfil` | Criar perfil de atleta
PUT | `/api/v1/atleta/perfil` | Atualizar perfil de atleta
GET | `/api/v1/eventos` | Listar eventos
POST | `/api/v1/eventos` | Criar novo evento
POST | `/api/v1/eventos/{id}/categorias` | Criar categoria do evento
POST | `/api/v1/inscricoes` | Criar inscrição
PUT | `/api/v1/lutas/{id}/resultado` | Lançar resultado da luta
Veja todas as rotas completas em: `/docs`

---

## 📁 Estrutura do Projeto
bjjeventos-api/
├── app/
│   ├── core/
│   │   ├── config.py
│   │   ├── deps.py
│   │   └── security.py
│   ├── models/
│   │   ├── atleta.py
│   │   ├── categoria.py
│   │   ├── evento.py
│   │   ├── inscricao.py
│   │   ├── luta.py
│   │   ├── perfil_atleta.py
│   │   └── usuario.py
│   ├── routers/
│   │   ├── atleta.py
│   │   ├── auth.py
│   │   ├── eventos.py
│   │   ├── inscricoes.py
│   │   └── usuarios.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── database.py
│   └── main.py
├── tests/
├── .env.example
├── requirements.txt
└── README.md
---

## ✅ Como Executar os Testes Automatizados
python run_tests.py
Ou:
py -m pytest -v
---

*Maria Luiza* - BJJEventOS

Esse agora tá 100% unido: manteve a matriz RBAC + as senhas de teste do primeiro, e a estrutura + tecnologias do segundo, mais o Git / Codespaces.

Quer que eu te passe o passo a passo de como colar ele lá no GitHub e dar o `push`?
