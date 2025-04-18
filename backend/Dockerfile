FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies and distutils
RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y python3-distutils \
    && apt-get install -y python3-dev \
    && apt-get install -y gcc \
    && rm -rf /var/lib/apt/lists/*  # Clean up apt cache to reduce image size

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy app code
COPY ./app ./app

# Run FastAPI with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
