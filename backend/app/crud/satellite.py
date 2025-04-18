from sqlalchemy.orm import Session
from .. import models, schemas

def create_satellite(db: Session, satellite: schemas.SatelliteCreate):
    db_sat = models.Satellite(**satellite.dict())
    db.add(db_sat)
    db.commit()
    db.refresh(db_sat)
    return db_sat

def get_satellites(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Satellite).offset(skip).limit(limit).all()
