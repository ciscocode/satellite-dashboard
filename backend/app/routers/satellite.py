from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud
from app.schemas.satellite import Satellite, SatelliteCreate
from app.database import SessionLocal

router = APIRouter(
    prefix="/satellites",
    tags=["satellites"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Satellite)
def create_satellite(satellite: SatelliteCreate, db: Session = Depends(get_db)):
    return crud.create_satellite(db, satellite)

@router.get("/", response_model=list[Satellite])
def read_satellites(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_satellites(db, skip=skip, limit=limit)
