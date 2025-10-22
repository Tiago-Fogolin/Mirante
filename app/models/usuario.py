from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class TipoPerfilEnum(str, enum.Enum):
    CIDADAO = "cidadão"
    PESQUISADOR = "pesquisador"
    GESTOR_PUBLICO = "gestor público"
    ADMIN = "admin"

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    tipo_perfil = Column(Enum(TipoPerfilEnum), nullable=False)
    municipio_id = Column(Integer, ForeignKey("municipios.id"), nullable=False)
    senha_hash = Column(String, nullable=False)

    municipio = relationship("Municipio", back_populates="usuarios")