# Use official Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy files into container
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Run the app
CMD ["python", "app.py"]
