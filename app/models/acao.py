from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum
from app.database import Base
from sqlalchemy.orm import relationship
import enum


class StatusAcaoEnum(enum.Enum):
    NAO_INICIADA = 0
    EM_ANDAMENTO = 1
    FINALIZADA   = 2

class Acao(Base):
    __tablename__ = "acoes"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    tema = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    data_inicio = Column(Date, nullable=False)
    status = Column(Enum(StatusAcaoEnum), nullable=False, default=StatusAcaoEnum.NAO_INICIADA)

    municipio_id = Column(Integer, ForeignKey("municipios.id"), nullable=False)

    municipio = relationship("Municipio", back_populates="acoes")


