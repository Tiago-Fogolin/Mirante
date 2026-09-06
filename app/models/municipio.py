from sqlalchemy import Column, Integer, String, Float
from app.database import Base
from sqlalchemy.orm import relationship


class Municipio(Base):
    __tablename__ = "municipios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    uf = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)

    usuarios = relationship("Usuario", back_populates="municipio")
    acoes = relationship("Acao", back_populates="municipio")
    noticias = relationship("Noticia", back_populates="municipio")
