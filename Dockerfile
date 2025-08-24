# Use modern supported Python version
FROM python:3.10-slim-bullseye

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . /app

# Install system dependencies (if needed for scientific libraries)
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run your app
CMD ["python", "app.py"]
