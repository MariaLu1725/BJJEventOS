from datetime import datetime, timedelta, date

def test_01_root_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

def test_02_cadastro_usuario_e_hash(client):
    payload = {"nome": "Marcus Buchecha", "email": "buchecha@bjj.com", "senha": "password123", "perfil": "atleta"}
    res = client.post("/api/v1/usuarios", json=payload)
    assert res.status_code == 201
    assert res.json()["email"] == "buchecha@bjj.com"

def test_03_login_e_token_jwt(client):
    client.post("/api/v1/usuarios", json={"nome": "Marcus Buchecha", "email": "buchecha2@bjj.com", "senha": "password123", "perfil": "atleta"})
    res = client.post("/api/v1/auth/login", data={"username": "buchecha2@bjj.com", "password": "password123"})
    assert res.status_code == 200
    assert "access_token" in res.json()

def test_04_rn01_email_duplicado(client):
    payload = {"nome": "Marcus Buchecha", "email": "buchecha_dup@bjj.com", "senha": "password123", "perfil": "atleta"}
    client.post("/api/v1/usuarios", json=payload)
    res = client.post("/api/v1/usuarios", json=payload)
    assert res.status_code == 400
    assert "Já existe uma conta" in res.json()["detail"]

def test_05_erro_401_unauthorized_sem_token(client):
    res = client.get("/api/v1/usuarios/me")
    assert res.status_code == 401

def test_06_erro_401_unauthorized_token_invalido(client):
    res = client.get("/api/v1/usuarios/me", headers={"Authorization": "Bearer token_invalido_123"})
    assert res.status_code == 401

def test_07_erro_403_forbidden_atleta_tenta_listar_usuarios(client):
    client.post("/api/v1/usuarios", json={"nome": "Atleta Teste", "email": "atleta_test7@bjj.com", "senha": "password123", "perfil": "atleta"})
    token = client.post("/api/v1/auth/login", data={"username": "atleta_test7@bjj.com", "password": "password123"}).json()["access_token"]
    res = client.get("/api/v1/usuarios", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 403

def test_08_erro_403_forbidden_atleta_tenta_criar_evento(client):
    client.post("/api/v1/usuarios", json={"nome": "Atleta Teste", "email": "atleta_test8@bjj.com", "senha": "password123", "perfil": "atleta"})
    token = client.post("/api/v1/auth/login", data={"username": "atleta_test8@bjj.com", "password": "password123"}).json()["access_token"]
    payload = {
        "nome": "Campeonato Proibido", "local_ginasio": "Ginásio A",
        "data_evento": (datetime.now() + timedelta(days=10)).isoformat(),
        "data_limite_inscricao": (datetime.now() + timedelta(days=5)).isoformat(),
        "data_checagem_geral": (datetime.now() + timedelta(days=7)).isoformat()
    }
    res = client.post("/api/v1/eventos", json=payload, headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 403

def test_09_organizador_cria_evento_e_categoria(client):
    client.post("/api/v1/usuarios", json={"nome": "Org Teste", "email": "org_test9@bjj.com", "senha": "password123", "perfil": "organizador"})
    token = client.post("/api/v1/auth/login", data={"username": "org_test9@bjj.com", "password": "password123"}).json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    ev_payload = {
        "nome": "BJJ Open 2026", "local_ginasio": "Ginásio Central",
        "data_evento": (datetime.now() + timedelta(days=10)).isoformat(),
        "data_limite_inscricao": (datetime.now() + timedelta(days=5)).isoformat(),
        "data_checagem_geral": (datetime.now() + timedelta(days=7)).isoformat()
    }
    ev_res = client.post("/api/v1/eventos", json=ev_payload, headers=headers)
    assert ev_res.status_code == 201
    ev_id = ev_res.json()["id"]

    cat_payload = {"modalidade": "Gi", "genero": "Masculino", "divisao_idade": "Adulto", "faixa": "Preta", "nome_categoria": "Pesadíssimo", "peso_limite_kg": 120.0}
    cat_res = client.post(f"/api/v1/eventos/{ev_id}/categorias", json=cat_payload, headers=headers)
    assert cat_res.status_code == 201

def test_10_fluxo_atleta_perfil_e_inscricao(client):
    client.post("/api/v1/usuarios", json={"nome": "Org Teste", "email": "org_test10@bjj.com", "senha": "password123", "perfil": "organizador"})
    token_org = client.post("/api/v1/auth/login", data={"username": "org_test10@bjj.com", "password": "password123"}).json()["access_token"]
    ev_payload = {
        "nome": "BJJ Open 2026", "local_ginasio": "Ginásio Central",
        "data_evento": (datetime.now() + timedelta(days=10)).isoformat(),
        "data_limite_inscricao": (datetime.now() + timedelta(days=5)).isoformat(),
        "data_checagem_geral": (datetime.now() + timedelta(days=7)).isoformat()
    }
    ev_id = client.post("/api/v1/eventos", json=ev_payload, headers={"Authorization": f"Bearer {token_org}"}).json()["id"]
    cat_payload = {"modalidade": "Gi", "genero": "Masculino", "divisao_idade": "Adulto", "faixa": "Preta", "nome_categoria": "Pesadíssimo", "peso_limite_kg": 120.0}
    cat_id = client.post(f"/api/v1/eventos/{ev_id}/categorias", json=cat_payload, headers={"Authorization": f"Bearer {token_org}"}).json()["id"]

    client.post("/api/v1/usuarios", json={"nome": "Atleta Teste", "email": "atleta_test10@bjj.com", "senha": "password123", "perfil": "atleta"})
    token_atl = client.post("/api/v1/auth/login", data={"username": "atleta_test10@bjj.com", "password": "password123"}).json()["access_token"]
    headers_atl = {"Authorization": f"Bearer {token_atl}"}

    perfil_payload = {"data_nascimento": "1995-05-20", "genero": "Masculino", "faixa": "Preta", "peso_atual_kg": 105.0, "academia_equipe": "Alliance"}
    perf_res = client.post("/api/v1/atleta/perfil", json=perfil_payload, headers=headers_atl)
    assert perf_res.status_code == 201

    insc_res = client.post("/api/v1/inscricoes", json={"categoria_id": cat_id}, headers=headers_atl)
    assert insc_res.status_code == 201
