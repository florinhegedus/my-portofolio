# Use the official Python image.
FROM python:3.11-slim

# Set the working directory.
WORKDIR /app

# Copy the requirements file and install dependencies.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code.
COPY . .

# Expose the port (optional, but good practice).
EXPOSE 8080

# Set environment variables (DigitalOcean provides $PORT).
ENV PORT=8080

# Run the application using Gunicorn.
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "app:app"]
