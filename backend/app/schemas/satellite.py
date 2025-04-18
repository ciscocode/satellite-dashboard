from pydantic import BaseModel

class SatelliteBase(BaseModel):
    name: str
    altitude: float
    velocity: float
    battery: float
    health_status: str

class SatelliteCreate(SatelliteBase):
    pass

class Satellite(SatelliteBase):
    id: int

    class Config:
        orm_mode = True
