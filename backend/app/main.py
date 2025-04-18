from fastapi import FastAPI
from .routers import satellite
from .database import engine
from .models import satellite as satellite_model

satellite_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(satellite.router)

@app.get("/")
def root():
    return {"message": "Satellite Dashboard API"}
