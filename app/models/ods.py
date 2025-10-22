from sqlalchemy import Column, Integer, String
from app.database import Base

class ODS(Base):
    __tablename__ = "ods"
    id = Column(Integer, primary_key=True, index=True)
    numero = Column(Integer, unique=True)
    nome = Column(String)
