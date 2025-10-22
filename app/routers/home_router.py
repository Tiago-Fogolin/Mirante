from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.services.home_service import HomeService



router = APIRouter(prefix="/home", tags=["home"])



@router.get("/")
def get_home_data(db: Session = Depends(get_db)):
    home_service = HomeService(db)
    return home_service.get_home_data()
