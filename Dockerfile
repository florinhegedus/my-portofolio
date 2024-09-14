# Use the official lightweight Python image.
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED True
ENV APP_HOME /app

# Set the working directory
WORKDIR $APP_HOME

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Expose port 8080
EXPOSE 8080

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
