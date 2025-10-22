from sqlalchemy.orm import Session
from app.models.ods import ODS as ODSModel
from app.schemas.ods import ODSCreate

class ODSService:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(ODSModel).all()
    
    def get_count(self):
        return self.db.query(ODSModel).count()
    
    def criar_ods(self, data: ODSCreate):
        db_ods = ODSModel(**data.model_dump())

        self.db.add(db_ods)
        self.db.commit()
        self.db.refresh(db_ods)

        return db_ods