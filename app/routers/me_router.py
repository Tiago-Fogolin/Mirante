from fastapi import APIRouter, Depends

from app.core.deps import get_current_user

from app.schemas.usuario import Usuario

router = APIRouter(prefix="/me", tags=["me"])

@router.get("/", response_model=Usuario)
def read_current_user(current_user: Usuario = Depends(get_current_user)):
    return current_user
