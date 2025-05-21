from fastapi import FastAPI
from .routers import satellite  # Import your router
from .database import init_db  # Import the init_db function to initialize DB
from .models import satellite as satellite_model  # Import models
from .database import engine  # You need to import engine for create_all

app = FastAPI()

# Initialize the database when the app starts
@app.on_event("startup")
def startup():
    init_db()  # Initialize database and create tables

# Create tables from models (if not already created)
satellite_model.Base.metadata.create_all(bind=engine)


# Include routers for handling requests
app.include_router(satellite.router)

@app.get("/")
def root():
    return {"message": "Satellite Dashboard API is up and running!"}
