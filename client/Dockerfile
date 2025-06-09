# Use official Python base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose app port (adjust per service if needed)
EXPOSE 8001

# Start the FastAPI server (adjust host/port if needed)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]
