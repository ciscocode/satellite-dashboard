# Satellite Dashboard
This project is Built using **FastAPI** for the backend, **Docker** for containerization, and **PostgreSQL** for database management. It is designed to simulate and display satellite-related data.

## Features
- FastAPI backend to manage satellite data.
- PostgreSQL database for storing satellite information.
- Dockerized environment for easy setup and deployment.
- Interactive dashboard to view and analyze satellite data (coming soon).

## Prerequisites

- **Docker**: For containerizing the backend and database.
- **Docker Compose**: To manage multi-container applications (backend and database).
- **Python 3.11+** (if you want to run outside Docker).

## Setup and Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ciscocode/satellite-dashboard.git
   cd satellite-dashboard

2. **Build and run with Docker Compose**:
    ```bash
    docker-compose up --build
    ```

This will build and start both the backend FastAPI app and the PostgreSQL database.

3. **Access the Application:**
- The FastAPI backend should now be running at http://localhost:8000.

- You can access the auto-generated documentation at http://localhost:8000/docs.


## Notes
- The project is containerized with Docker, but you can also run it locally without Docker if preferred.

- The database uses PostgreSQL, and environment variables are configured in the .env file.




