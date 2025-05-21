from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Satellite(Base):
    __tablename__ = 'satellites'  # This is the name of the table in the DB
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # ID field as primary key
    name = Column(String, nullable=False)  # Name of the satellite (cannot be empty)
    country = Column(String, nullable=False)  # Country of the satellite operator (cannot be empty)
    purpose = Column(String, nullable=False)  # Purpose of the satellite (cannot be empty)
    latitude = Column(Float, nullable=False)  # Latitude position of the satellite (cannot be empty)
    longitude = Column(Float, nullable=False)  # Longitude position of the satellite (cannot be empty)
    altitude = Column(Float, nullable=False)  # Altitude position of the satellite (cannot be empty)
    velocity = Column(Float, nullable=False)  # Velocity of the satellite (cannot be empty)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)  # Timestamp of the data (cannot be empty)
    battery = Column(Float, nullable=False)  # Battery level of the satellite (cannot be empty)