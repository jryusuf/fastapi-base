# Use an official Python image as the base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose port 80
EXPOSE 80

# Run the application with Uvicorn on port 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
