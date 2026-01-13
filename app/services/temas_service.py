from sqlalchemy.orm import Session
from app.models.tema import Tema as TemaModel
from app.schemas.tema import TemaCreate

class TemaService:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(TemaModel).all()

    def get_count(self):
        return self.db.query(TemaModel).count()

    def get_by_id(self, id):
        return self.db.query(TemaModel).get(id)

    def criar_tema(self, data: TemaCreate):
        db_acao = TemaModel(**data.model_dump())
        self.db.add(db_acao)
        self.db.commit()
        self.db.refresh(db_acao)
        return db_acao
