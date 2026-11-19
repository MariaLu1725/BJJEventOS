from fastapi import FastAPI
from app.core.config import settings
from app.database import engine, Base
from app.models import Usuario, PerfilAtleta, Evento, Categoria, Inscricao, Luta
from app.routers import auth, usuarios, atleta, eventos, categorias, inscricoes, lutas

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(auth.router, prefix=settings.API_V1_STR)
app.include_router(usuarios.router, prefix=settings.API_V1_STR)
app.include_router(atleta.router, prefix=settings.API_V1_STR)
app.include_router(eventos.router, prefix=settings.API_V1_STR)
app.include_router(categorias.router, prefix=settings.API_V1_STR)
app.include_router(inscricoes.router, prefix=settings.API_V1_STR)
app.include_router(lutas.router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {"sistema": settings.PROJECT_NAME, "versao": settings.VERSION, "status": "online", "docs": "/docs"}
