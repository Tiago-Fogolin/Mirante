from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import municipios_router
from app.routers import usuarios_router
from app.routers import acoes_router
from app.routers import ods_router
from app.routers import home_router
from app.routers import me_router
from app.routers import temas_router


app = FastAPI(title="Mirante API")


origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(municipios_router.router)
app.include_router(usuarios_router.router)
app.include_router(acoes_router.router)
app.include_router(ods_router.router)
app.include_router(home_router.router)
app.include_router(me_router.router)
app.include_router(temas_router.router)
