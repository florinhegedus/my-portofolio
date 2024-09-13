# Use the official Python image.
FROM python:3.11-slim

# Set the working directory.
WORKDIR /app

# Copy the requirements file and install dependencies.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code.
COPY . .

# Expose port 8080.
EXPOSE 8080

# Set environment variables.
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

# Run the application.
CMD ["flask", "run"]
