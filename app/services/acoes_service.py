from sqlalchemy.orm import Session
from app.models.acao import Acao as AcaoModel
from app.schemas.acao import AcaoCreate

class AcaoService:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(AcaoModel).all()
    
    def get_by_id(self, id):
        return self.db.query(AcaoModel).get(id)

    def criar_acao(self, data: AcaoCreate):
        db_acao = AcaoModel(**data.model_dump())
        self.db.add(db_acao)
        self.db.commit()
        self.db.refresh(db_acao)
        return db_acao
    
