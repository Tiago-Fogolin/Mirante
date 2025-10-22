from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.services.home_service import HomeService
from app.schemas.home import HomeResponse


router = APIRouter(prefix="/home", tags=["home"])



@router.get("/", response_model=HomeResponse)
def get_home_data(db: Session = Depends(get_db)):
    home_service = HomeService(db)
    return home_service.get_home_data()
