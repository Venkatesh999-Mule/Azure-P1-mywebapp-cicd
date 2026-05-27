# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependencies file first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files
COPY . .

# Expose port 8000
EXPOSE 8000

# Start the app using gunicorn (production server)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "app:app"]
