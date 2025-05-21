from sqlalchemy import Column, Integer, String, Float
from app.database import Base 

class Satellite(Base):
    __tablename__ = "satellites"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    altitude = Column(Float)
    velocity = Column(Float)
    battery = Column(Float)
    health_status = Column(String)