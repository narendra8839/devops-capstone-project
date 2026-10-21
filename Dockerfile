FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY service/ ./service/

# Create a non-root user for security
RUN useradd --uid 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port 8080
EXPOSE 8080

# Run the service using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "service:app"]
