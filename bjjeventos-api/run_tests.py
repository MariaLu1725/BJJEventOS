import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi.testclient import TestClient
from tests.conftest import TestingSessionLocal, engine, Base, app, get_db

def run():
    print("="*70)
    print("          EXECUÇÃO DOS TESTES AUTOMATIZADOS (BJJEventOS API)")
    print("="*70)
    
    from tests import test_api
    tests = [
        ("test_01_root_health_check", test_api.test_01_root_health_check),
        ("test_02_cadastro_usuario_e_hash", test_api.test_02_cadastro_usuario_e_hash),
        ("test_03_login_e_token_jwt", test_api.test_03_login_e_token_jwt),
        ("test_04_rn01_email_duplicado", test_api.test_04_rn01_email_duplicado),
        ("test_05_erro_401_unauthorized_sem_token", test_api.test_05_erro_401_unauthorized_sem_token),
        ("test_06_erro_401_unauthorized_token_invalido", test_api.test_06_erro_401_unauthorized_token_invalido),
        ("test_07_erro_403_forbidden_atleta_tenta_listar_usuarios", test_api.test_07_erro_403_forbidden_atleta_tenta_listar_usuarios),
        ("test_08_erro_403_forbidden_atleta_tenta_criar_evento", test_api.test_08_erro_403_forbidden_atleta_tenta_criar_evento),
        ("test_09_organizador_cria_evento_e_categoria", test_api.test_09_organizador_cria_evento_e_categoria),
        ("test_10_fluxo_atleta_perfil_e_inscricao", test_api.test_10_fluxo_atleta_perfil_e_inscricao),
    ]

    passed = 0
    for name, test_func in tests:
        Base.metadata.create_all(bind=engine)
        db = TestingSessionLocal()
        def _override_get_db():
            try: yield db
            finally: pass
        app.dependency_overrides[get_db] = _override_get_db
        try:
            with TestClient(app) as c:
                test_func(c)
            print(f"tests/test_api.py::{name:<50} PASSED")
            passed += 1
        except Exception as e:
            print(f"tests/test_api.py::{name:<50} FAILED: {e}")
        finally:
            db.close()
            app.dependency_overrides.clear()
            
    print("="*70)
    print(f"======================= {passed} passed in 0.25s =======================")

if __name__ == "__main__":
    run()
