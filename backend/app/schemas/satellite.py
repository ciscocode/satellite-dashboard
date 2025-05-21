from pydantic import BaseModel

class SatelliteBase(BaseModel):
    name: str
    altitude: float
    velocity: float
    battery: float
    health_status: str
    latitude: float
    longitude: float
    heading: float | None = None  # optional

class SatelliteCreate(SatelliteBase):
    pass

class Satellite(SatelliteBase):
    id: int

    class Config:
        from_attributes = True
