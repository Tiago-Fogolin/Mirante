from logging import NullHandler
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

acao_temas_association = Table(
    'acao_temas',
    Base.metadata,
    Column('acao_id', Integer, ForeignKey('acoes.id'), primary_key=True),
    Column('tema_id', Integer, ForeignKey('temas.id'), primary_key=True)
)

class Tema(Base):
    __tablename__ = "temas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    descricao = Column(String, nullable=True)

    acoes = relationship(
        "Acao",
        secondary=acao_temas_association,
        back_populates="temas"
    )
