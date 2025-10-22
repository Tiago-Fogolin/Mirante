from sqlalchemy.orm import Session
from app.models.usuario import Usuario as UsuarioModel
from app.schemas.usuario import UsuarioCreate
from app.core.security import create_access_token
from passlib.context import CryptContext
from typing import Optional
from datetime import timedelta


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UsuarioService:

    def __init__(self, db: Session):
        self.db = db

    def criar_usuario(self, data: UsuarioCreate):
        senha_hash = pwd_context.hash(data.senha)

        usuario = UsuarioModel(
            nome = data.nome,
            email = data.email,
            tipo_perfil = data.tipo_perfil,
            municipio_id = data.municipio_id,
            senha_hash = senha_hash
        )

        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)

        return usuario

    def verificar_credenciais(self, email: str, senha: str) -> Optional[UsuarioModel]:
        usuario = self.db.query(UsuarioModel).filter(UsuarioModel.email == email).first()
        
        if not usuario:
            return None
        if not pwd_context.verify(senha, usuario.senha_hash):
            return None
        
        return usuario

    def criar_usuario_com_token(self, data: UsuarioCreate):
        usuario = self.criar_usuario(data)
        token = create_access_token(
            data={"sub": usuario.email},
            expires_delta=timedelta(minutes=60)
        )
        return usuario, token