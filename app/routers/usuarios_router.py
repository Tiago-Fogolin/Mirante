from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.usuario import UsuarioCreate
from app.schemas.auth import Token, LoginRequest
from app.models.usuario import Usuario
from app.dependencies import get_db
from app.core.security import create_access_token
from app.services.usuario_service import UsuarioService
from sqlalchemy.exc import IntegrityError


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=Token)
def registrar(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    service = UsuarioService(db)

    # TODO -> mudar pra service essa query do existente
    existente = db.query(Usuario).filter_by(email=usuario.email).first()
    if existente:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")
    try:
        _, token = service.criar_usuario_com_token(usuario)

        retorno = {
            "access_token": token, 
            "token_type": "bearer"
        }

        return retorno
    except IntegrityError as e:
        db.rollback() 

        if 'chave' in str(e.orig).lower():
            raise HTTPException(
                status_code=400,
                detail="O município informado não existe"
            )

        raise HTTPException(
            status_code=400,
            detail="Erro de integridade ao criar usuário"
        )
    
@router.post("/login", response_model=Token)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    service = UsuarioService(db)
    usuario = service.verificar_credenciais(request.username, request.password)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")

    token = create_access_token({"sub": usuario.email})
    return {"access_token": token, "token_type": "bearer"}
