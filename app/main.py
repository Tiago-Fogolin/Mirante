from fastapi import FastAPI
from app.routers import municipios_router
from app.routers import usuarios_router
from app.routers import acoes_router

app = FastAPI(title="Mirante API")

app.include_router(municipios_router.router)
app.include_router(usuarios_router.router)
app.include_router(acoes_router.router)

