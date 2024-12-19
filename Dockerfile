FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Run the application with gunicorn for production
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
