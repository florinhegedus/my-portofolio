# Portfolio Website
This is my portofolio, it will be a website with all the relevant things about my projects.

# Steps to reproduce

## Test locally
Create an env locally (e.g. with conda), add app.py and requirements.txt and test the functionality.
```
python app.py
```

## Containerize application
Create the Dockerfile and build the image.
```
docker build -t flask-app .
```

Test the container locally.
```
docker run -p 8080:8080 flask-app
```

## Upload image to Google Cloud
Login to google cloud.
```
gcloud auth login
```

Set project.
```
gcloud config set project your-project-id
```

Enable necessary services.
```
gcloud services enable containerregistry.googleapis.com
gcloud services enable run.googleapis.com
```

Tag the docker image.
```
docker tag flask-app gcr.io/your-project-id/flask-app
```

Authenticate docker for access to gc.
```
gcloud auth configure-docker
```

Push the image.
```
docker push gcr.io/your-project-id/flask-app
```

## Deploy the app
```
gcloud run deploy flask-app \
  --image gcr.io/your-project-id/flask-app \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## How to stop the app
Delete the service.
```
gcloud run services delete flask-app --platform managed --region us-central1
```

Delete the container.
```
gcloud container images delete gcr.io/your-project-id/flask-app --force-delete-tags
```
