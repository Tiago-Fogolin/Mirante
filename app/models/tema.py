from logging import NullHandler
from sqlalchemy import Column, Integer, String, Date
from app.database import Base
from sqlalchemy.orm import relationship


class Tema(Base):
    __tablename__ = "temas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    descricao = Column(String, nullable=True)
