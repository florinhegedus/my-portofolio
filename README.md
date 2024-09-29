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
gcloud config set project steam-link-435607-q6
```

Enable necessary services.
```
gcloud services enable containerregistry.googleapis.com
gcloud services enable run.googleapis.com
```

Tag the docker image.
```
docker tag flask-app gcr.io/steam-link-435607-q6/flask-app
```

Authenticate docker for access to gc.
```
gcloud auth configure-docker
```

Push the image.
```
docker push gcr.io/steam-link-435607-q6/flask-app
```

## Deploy the app
```
gcloud run deploy flask-app --image gcr.io/steam-link-435607-q6/flask-app --platform managed --region us-central1 --allow-unauthenticated
```

## Add secret
You can add a secret from `Edit CICD` - `Container`. Then you should grant the service user permissions to access the secret:
```
gcloud secrets add-iam-policy-binding SECRET_YOU_WANT --member="serviceAccount:9826031314-compute@developer.gserviceaccount.com" --role="roles/secretmanager.secretAccessor"
```


## How to stop the app
Delete the service.
```
gcloud run services delete flask-app --platform managed --region us-central1
```

Delete the container.
```
gcloud container images delete gcr.io/steam-link-435607-q6/flask-app --force-delete-tags
```

## Add a custom domain
Go to gc network services, cloud DNS and create a zone.
Go to cloud domains and create your custom domain. Change the DNS to cloud DNS, from the dropdown select the zone that you created before.
In cloud run, go to manage custom domains and add your desired subdomain, copy the DNS to the table of DNSes in cloud DNS.
