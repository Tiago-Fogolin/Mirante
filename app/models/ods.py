from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.noticia import noticia_ods_association

class ODS(Base):
    __tablename__ = "ods"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(Integer, unique=True)
    nome = Column(String)

    acao_ods = relationship("AcaoOds", back_populates="ods", cascade="all, delete-orphan")
    noticias = relationship(
        "Noticia",
        secondary=noticia_ods_association,
        back_populates="ods"
    )
