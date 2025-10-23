from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum
from app.database import Base
from sqlalchemy.orm import relationship



class AcaoOds(Base):
    __tablename__ = "acao_ods"
    
    acao_id = Column(Integer, ForeignKey("acoes.id"), primary_key=True)
    ods_id = Column(Integer, ForeignKey("ods.id"), primary_key=True)

    acao = relationship("Acao", back_populates="acao_ods")
    ods  = relationship("ODS", back_populates="acao_ods")