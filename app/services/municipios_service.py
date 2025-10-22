from sqlalchemy.orm import Session
from app.models.municipio import Municipio as MunicipioModel
from app.schemas.municipio import MunicipioCreate

class MunicipioService:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MunicipioModel).all()
    
    def get_by_id(self, id):
        return self.db.query(MunicipioModel).get(id)

    def criar_municipio(self, data: MunicipioCreate):
        db_municipio = MunicipioModel(**data.model_dump())
        self.db.add(db_municipio)
        self.db.commit()
        self.db.refresh(db_municipio)
        return db_municipio
    
