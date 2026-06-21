# Use Python image
FROM python:3.13-slim

# Create working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run program
CMD ["python", "main.py"]